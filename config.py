import os
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


try:
    COHERE_API_KEY = st.secrets["COHERE_API_KEY"]
except Exception:
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")


# -----------------------------
# LLM
# -----------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0
)

system_prompt = """
You are an Enterprise AI Assistant.

Rules:

1. Answer ONLY from company documents and company database.
2. If the answer is unavailable, say:
'I couldn't find that information in the company knowledge base.'

3. Never make up answers.

4. Keep answers professional and concise.
"""


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("placeholder", "{messages}")
    ]
)