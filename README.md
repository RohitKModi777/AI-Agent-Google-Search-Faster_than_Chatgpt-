# 🚀 AI-Agent-Google-Search - Faster than ChatGPT

A cutting-edge AI Agent that uses Large Language Models (LLMs) and real-time Google Search to provide accurate, data-backed answers at lightning-fast speeds.

## ✨ Core Features
- **Real-time Web Browsing:** Uses the Google Serper API to fetch live information from the internet.
- **Ultra-Fast Reasoning:** Powered by **Groq (Llama-3/Mixtral)** for instant response generation.
- **Context-Aware Conversations:** Advanced memory management ensures the bot remembers previous questions and maintains context.
- **Streamlined Chat UI:** Modern interactive interface built with **Streamlit**.
- **Live Streaming:** Responses are streamed chunk-by-chunk for a more natural user experience.

## 🛠️ How it Works ⚙️

### 🌐 Google Search Integration
The agent is connected to the web via the **Google Serper API**. Unlike standard chatbots that rely solely on their training data (which may be outdated), this agent:
1.  **Analyzes the Query:** The LLM determine if a search is required.
2.  **Executes Search:** It calls the `GoogleSerperAPIWrapper` to retrieve relevant search results.
3.  **Synthesizes Results:** It reads the search snippets and crafts a comprehensive answer, effectively browsing the web on your behalf.

### 🧠 Advanced History Management
To maintain a natural flow of conversation, the bot implements a dual-layer history system:
-   **LangGraph MemorySaver:** This acts as a 'checkpointer' for the AI Agent. It saves the entire conversation state in memory, allowing the agent to remember context (e.g., if you ask "Who is Obama?" followed by "How old is he?", the agent knows "he" refers to Obama).
-   **Streamlit Session State:** We use `st.session_state.history` to store and render the chat bubbles on the frontend, ensuring the conversation remains visible throughout the user session.

## 🚀 Getting Started 💻

### 1. Prerequisites
- Python 3.10 or higher.
- API Keys for [Groq](https://console.groq.com/) and [Serper](https://serper.dev/).

### 2. Installation
```bash
git clone https://github.com/RohitKModi777/AI-Agent-Google-Search-Faster_than_Chatgpt-.git
cd AI-Agent-Google-Search-Faster_than_Chatgpt-
pip install -r requirements.txt
```

### 3. Configuration 🔑
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_key_here
SERPER_API_KEY=your_serper_google_search_key_here
```

### 4. Running the Bot
```bash
streamlit run ai_agent_google_search.py
```

## 🌐 Deployment Logic 🚀

This application is ready for deployment on **Streamlit Cloud**:
- Link your GitHub repository.
- Set the main file to `ai_agent_google_search.py`.
- Add your `.env` keys to **Settings > Secrets** in the Streamlit Cloud dashboard.

---
