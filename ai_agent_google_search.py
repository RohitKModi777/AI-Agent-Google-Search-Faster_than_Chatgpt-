
from dotenv import load_dotenv 
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper # Library to perform Google Search using Serper API
from langchain_groq import ChatGroq 
from langchain.agents import create_agent # To create an intelligent agent capable of autonomous tool usage
from langgraph.checkpoint.memory import MemorySaver # To save conversation history for the agent, enabling context-aware chat
import streamlit as st 


model = ChatGroq(model="openai/gpt-oss-20b", streaming=True) 

# Setting up Google Search capability via Serper API
search = GoogleSerperAPIWrapper()
tools = [search.run] # Giving the agent access to the search tool to fetch real-time info from the web

# Setting up Memory 🧠 
# Check if memory exists in the session, if not, initialize it to store chat history.
if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver() # Keeps track of thread-specific context for multi-turn conversations
    st.session_state.history = [] # Stores user-ai conversation history for frontend display


agent = create_agent(
    model=model,
    tools=tools,
    checkpointer=st.session_state.memory, # Connects the agent logic with the memory saver
    system_prompt="You are an agent and can search any question on google and answer it.",
)


st.header("🤖 AI-Search Agent - Faster than ChatGPT")
st.subheader("🗨️ QuickAnswer - Answer at the speed of thought")


for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Anything.. ")


if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role": "user", "content": query})
    

    response = agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "1"}}, # Maintains session state across multiple queries
        stream_mode="messages"
    )
    
    # AI response container for real-time streaming display
    ai_container = st.chat_message("ai")
    with ai_container:
        space = st.empty()
        full_message = ""

        
        for chunk in response:
            full_message += chunk[0].content
            space.write(full_message) 
        
        st.session_state.history.append({"role": "ai", "content": full_message})
