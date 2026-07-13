import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS

import streamlit as st

from config import COHERE_API_KEY


documents=[]

data_folder="data"

for file in os.listdir(data_folder):
    if file.endswith(".pdf"):
        loader=PyPDFLoader(os.path.join(data_folder,file))
        documents.extend(loader.load())


# --------------------------------------
# Split Documents
# --------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = text_splitter.split_documents(
    documents
)


# --------------------------------------
# Embeddings
# --------------------------------------

embeddings = CohereEmbeddings(
    model="embed-english-v3.0",
    cohere_api_key=COHERE_API_KEY
)


# --------------------------------------
# Create Vector Database
# --------------------------------------

VECTOR_DB = "vectorstore"


if os.path.exists(VECTOR_DB):

    vectorstore = FAISS.load_local(
        VECTOR_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )

else:

    vectorstore = FAISS.from_documents(
        docs,
        embeddings
    )

    vectorstore.save_local(VECTOR_DB)

# --------------------------------------
# Retriever
# --------------------------------------

retriever = vectorstore.as_retriever(
    search_kwargs={
        "k":4
    }
)