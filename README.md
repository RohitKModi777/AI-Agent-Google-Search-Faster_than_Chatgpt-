# 🚀 AI-Agent-Google-Search-Faster-than-ChatGPT

A powerful AI Agent that uses advanced LLMs and Google Search to fetch real-time answers. This bot is designed for speed and accuracy, surpassing standard chat experiences by browsing the web when needed.

## ✨ Features
- **Real-time Search:** Uses Google Serper API to fetch the latest information.
- **Advanced Reasoning:** Built with **Groq (Llama-3/Mixtral)** for lightning-fast reasoning.
- **Smart Memory:** Maintains context across conversations using **LangGraph MemorySaver**.
- **Interactive UI:** A sleek and modern chat interface built with **Streamlit**.
- **Streaming Output:** View answers as they are generated, character-by-character.

## 🛠️ Tech Stack
- **LangChain & LangGraph:** For agent orchestration and memory.
- **Groq AI:** To leverage ultra-fast inference speed.
- **Google Serper API:** For real-time web search capabilities.
- **Streamlit:** For a responsive web frontend.

## 🚀 How to Run Locally 💻

### 1. Prerequisite
Ensure you have **Python 3.10+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/RohitKModi777/AI-Agent-Google-Search-Faster_than_Chatgpt-.git
cd AI-Agent-Google-Search-Faster_than_Chatgpt-
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Setup Environment Variables 🔑
Create a `.env` file in the root directory and add your API keys:
```env
GROQ_API_KEY=your_groq_key_here
SERPER_API_KEY=your_serper_google_search_key_here
```

### 6. Run the Application
```bash
streamlit run ai_agent_google_search.py
```

## 🌐 Deployment Logic 🚀

This app is ready for deployment on **Streamlit Cloud** or **Vercel**.
- **Streamlit Cloud:** Just link this GitHub repository, select `ai_agent_google_search.py` as the main file, and add your `.env` keys to the **Secrets manager (Settings > Secrets)**.

## 📚 Educational Notes (Student Perspective) 🎓
The code has been commented with 'student-style' notes to help you understand:
- **What** each library does.
- **Why** we are using an Agent for search.
- **How** memory and streaming work in a modern LLM app.

---
Developed by [RohitKModi777](https://github.com/RohitKModi777) 💡
