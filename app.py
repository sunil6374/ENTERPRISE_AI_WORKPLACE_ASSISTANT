import streamlit as st

from langchain_core.messages import HumanMessage

from graph import graph


# --------------------------------------
# Streamlit Page
# --------------------------------------

st.set_page_config(
    page_title="Enterprise AI Assistant",
    page_icon="🤖"
)

st.title("🤖 Enterprise AI Assistant")


# --------------------------------------
# Session State
# --------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "enterprise_user"


# --------------------------------------
# Display Chat History
# --------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])
# --------------------------------------
# User Input
# --------------------------------------pp
        
if prompt := st.chat_input("Ask anything about your company..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }
    
    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=prompt)
            ]
        },
        config=config
    )

    response = result["messages"][-1].content

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):

        st.markdown(response)
    
    

