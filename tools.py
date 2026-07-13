from langchain_core.tools import tool
from langchain_community.utilities import SQLDatabase

from rag import retriever


# ------------------------------------------------
# Database
# ------------------------------------------------

db=SQLDatabase.from_uri(
    "sqlite:///database/company.db"
)


# ------------------------------------------------
# RAG Tool
# ------------------------------------------------

@tool
def retrive_information(query:str)->str:
    '''Creating retriever chain'''
    docs=retriever.invoke(query)
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )
    

# ------------------------------------------------
# SQL Tool (db to be defined lated)
# ------------------------------------------------

@tool
def company_database(query:str)->str:
    '''Creating company db'''
    
    try:
        result=db.run(query)
        return str(result)
    except Exception as e:
            return str(e)
        

# ------------------------------------------------
# Tool List
# ------------------------------------------------

tools=[
    retrive_information,
    company_database
]
    
    
    

    
