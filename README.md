# 🏢 Enterprise AI Workplace Assistant

An intelligent Enterprise AI Assistant built using **LangGraph**, **LangChain**, **Groq LLM**, **FAISS**, and **Streamlit**. The assistant answers employee questions by combining information from company PDF documents and an internal database while maintaining conversational memory.

---

## 🚀 Features

* 📄 Retrieval-Augmented Generation (RAG)
* 🧠 Conversation Memory using LangGraph Checkpointing
* 💬 Multi-Chat Support with unique Thread IDs
* ⚡ Cached FAISS Vector Store for faster startup
* 🔎 Semantic Search over company PDF documents
* 🗄️ Database integration for structured company information
* 🤖 Groq LLM (Llama 3.3 70B Versatile)
* 🌐 Interactive Streamlit Web Interface
* 📚 Professional System Prompt to reduce hallucinations
* 🔄 Streaming responses using LangGraph events

---

## 🏗️ Architecture

```text
                        User
                          │
                          ▼
                  Streamlit Interface
                          │
                          ▼
                    LangGraph Agent
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
     FAISS Retriever              Company Database
            │                           │
            ▼                           ▼
     Company PDF Files          Structured Information
            │                           │
            └─────────────┬─────────────┘
                          ▼
                    Groq LLM
                          │
                          ▼
                   Final Response
```

---

## 🛠️ Tech Stack

* Python
* LangGraph
* LangChain
* LangChain Community
* Groq API
* FAISS
* Cohere / Google Embeddings
* SQLite
* Streamlit
* Pydantic

---

## 📂 Project Structure

```text
Enterprise_AI_Workplace_Assistant/

│
├── app.py
├── config.py
├── graph.py
├── rag.py
├── state.py
├── tools.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── company_policy.pdf
│   └── employee_handbook.pdf
│
├── database/
│   └── company.db
│
└── vectorstore/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd Enterprise_AI_Workplace_Assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
python -m pip install -r requirements.txt
```

Run the application

```bash
python -m streamlit run app.py
```

---

## 🔑 Environment Variables

Create a `.env` file for local development.

```text
GROQ_API_KEY=your_groq_api_key
COHERE_API_KEY=your_cohere_api_key
```

For Streamlit Cloud, add the same values under **App Settings → Secrets**.

---

## 💡 Example Questions

* What is the company's leave policy?
* How many casual leaves are available?
* Explain the work-from-home policy.
* What are the office timings?
* What documents are required for onboarding?

---

## 📈 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* LangGraph StateGraph
* Memory & Checkpointing
* Tool Calling
* Vector Databases (FAISS)
* Semantic Search
* Prompt Engineering
* Streamlit Deployment
* Enterprise AI Workflows

---

## 🎯 Future Enhancements

* PDF Upload from UI
* Source Citations
* Token-by-token Streaming
* User Authentication
* Role-Based Access Control
* Multi-Agent Architecture
* MCP Integration
* Cloud Database Support

---

## 👨‍💻 Author

Developed as part of an AI Engineering portfolio to demonstrate practical enterprise-grade applications using modern LLM frameworks such as LangGraph and LangChain.
