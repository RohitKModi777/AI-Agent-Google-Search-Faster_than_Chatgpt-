# AI-Search-Agent-Google 🔎
# This application is an advanced AI Agent that uses an LLM (Groq) and Google Search (Serper)
# to providing real-time, accurate answers to any question with the context of Google Search.

# Importing Necessary Libraries 📚
from dotenv import load_dotenv # Used for loading environment variables like API keys from .env file
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper # Library to perform Google Search using Serper API
from langchain_groq import ChatGroq # Groq interface to use fast LLMs like Llama or Mixtral for reasoning
from langchain.agents import create_agent # To create an intelligent agent capable of autonomous tool usage
from langgraph.checkpoint.memory import MemorySaver # To save conversation history for the agent, enabling context-aware chat
import streamlit as st # Modern web framework for building interactive user interfaces quickly

# Initializing LLM and Tools 🛠️
# Setting up Groq as our Large Language Model (LLM) with streaming enabled for a smoother user experience
model = ChatGroq(model="openai/gpt-oss-20b", streaming=True) 

# Setting up Google Search capability via Serper API
search = GoogleSerperAPIWrapper()
tools = [search.run] # Giving the agent access to the search tool to fetch real-time info from the web

# Setting up Memory 🧠 
# Check if memory exists in the session, if not, initialize it to store chat history.
if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver() # Keeps track of thread-specific context for multi-turn conversations
    st.session_state.history = [] # Stores user-ai conversation history for frontend display

# Defining the Agent 🤖
# This agent acts as a reasoning engine that decides when to search Google and how to process the results.
agent = create_agent(
    model=model,
    tools=tools,
    checkpointer=st.session_state.memory, # Connects the agent logic with the memory saver
    system_prompt="You are an agent and can search any question on google and answer it.",
)

# Building Web Interface with Streamlit 🌐
st.header("🤖 AI-Search Agent - Faster than ChatGPT")
st.subheader("🗨️ QuickAnswer - Answer at the speed of thought")

# Displaying chat history from session state to maintain the chat-like interface
for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

# Input for User Query ✍️
# Using st.chat_input for a modern and sleek chat-like user interaction
query = st.chat_input("Ask Anything.. ")

# Handling User Input and Generating Response
if query:
    # Display user's message immediately for responsive feel
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role": "user", "content": query})
    
    # Getting AI response from the agent with streaming ⚡
    # The agent decides to use Google Search if the query requires external information
    response = agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "1"}}, # Maintains session state across multiple queries
        stream_mode="messages"
    )
    
    # AI response container for real-time streaming display
    ai_container = st.chat_message("ai")
    with ai_container:
        space = st.empty() # Placeholder for streaming text updates
        full_message = ""

        # Processing streaming chunks from the AI response
        for chunk in response:
            full_message += chunk[0].content
            space.write(full_message) # Dynamic UI update with each new token/chunk
        
        # Save complete AI response to history for persistence in the current session
        st.session_state.history.append({"role": "ai", "content": full_message})
