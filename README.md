# 🏏 AI Sports Quiz Generator

An AI-powered Sports Quiz Generator that creates dynamic multiple-choice quizzes using **Google Gemini**, **ChromaDB (RAG)**, and **live sports news** from DuckDuckGo.

Instead of relying on a fixed question bank, the application retrieves historical sports facts from a vector database and combines them with the latest sports news to generate unique quizzes in real time.

---

## 🚀 Features

- 🤖 AI-generated quiz questions using Google Gemini
- 📚 Retrieval-Augmented Generation (RAG) with ChromaDB
- 📰 Live sports news integration using DuckDuckGo Search
- 🎯 Difficulty Levels (Easy, Medium, Hard)
- 🏆 Multiple sports support
  - Cricket
  - Football
  - Basketball
  - Tennis
- ✅ Automatic scoring
- 💡 AI-generated explanations for every answer
- 🔒 Answers locked after quiz submission
- 🎨 Interactive Streamlit interface
- 📄 Structured JSON responses using Pydantic

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI
- Google Gemini API

### Vector Database
- ChromaDB

### Search
- DuckDuckGo Search (DDGS)

### Data Validation
- Pydantic

### Environment Management
- python-dotenv

---

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
               Streamlit UI
                      │
      ┌───────────────┴───────────────┐
      │                               │
      ▼                               ▼
 ChromaDB (Historical Facts)     DuckDuckGo Search
      │                               │
      └───────────────┬───────────────┘
                      ▼
              Prompt Engineering
                      │
                      ▼
               Google Gemini API
                      │
                      ▼
          Structured Quiz (JSON)
                      │
                      ▼
               Streamlit Interface

'''
sports-quiz-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   └── sports_facts.json
│
├── chroma_db/
│
└── src/
    ├── config.py
    ├── database.py
    ├── generator.py
    ├── prompts.py
    ├── schema.py
    ├── search.py
    └── utils.py


               
