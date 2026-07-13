from langchain_core.tools import tool
from langchain_community.utilities import SQLDatabase
from langchain_classic.chains import create_sql_query_chain

from rag import retriever

from config import llm

# ------------------------------------------------
# Database
# ------------------------------------------------

db=SQLDatabase.from_uri(
    "sqlite:///database/company.db"
)
sql_chain = create_sql_query_chain(
    llm=llm,
    db=db
)

# ------------------------------------------------
# RAG Tool
# ------------------------------------------------

@tool
def retrieve_information(query:str)->str:
    '''Search the company PDF documents and return relevant information.
    Use this tool whenever the user asks about company policies,
    manuals, employee handbook, Holy Qurbana, Sunday School content,
    or any information contained in the PDF documents.'''
    docs=retriever.invoke(query)
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return "\n\n".join(doc.page_content for doc in docs)
    

# ------------------------------------------------
# SQL Tool 
# ------------------------------------------------

@tool
def company_database(question: str) -> str:
    """
    Query the company SQLite database using natural language.
    """

    try:

        sql = sql_chain.invoke(
            {
                "question": question
            }
        )
        print(sql)

        # Extract only the SQL part
        if "SQLQuery:" in sql:
            sql = sql.split("SQLQuery:")[-1].strip()

        result = db.run(sql)

        return str(result)
        print("SQL =", sql)
        print("RESULT =", result)
    
    

        

    except Exception as e:
        return str(e)

# ------------------------------------------------
# Tool List
# ------------------------------------------------

tools=[
    retrieve_information,
    company_database
]
