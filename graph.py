from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

from langchain_core.messages import HumanMessage

from config import llm,prompt
from tools import tools
from state import State


# ---------------------------------------------------
# Bind tools to LLM
# ---------------------------------------------------

llm = llm.bind_tools(tools)


# ---------------------------------------------------
# Chatbot Node
# ---------------------------------------------------
def chatbot(state: State):
    chain=prompt | llm

    response = chain.invoke(
    {
        "messages": state["messages"]
    }
)

    return {
        "messages": [response]
    }


# ---------------------------------------------------
# Build Graph
# ---------------------------------------------------

builder = StateGraph(State)

builder.add_node(
    "chatbot",
    chatbot
)
builder.add_node(
    "tools",
    ToolNode(tools)
)


# ---------------------------------------------------
# Edges
# ---------------------------------------------------

builder.add_edge(
    START,
    "chatbot"
)

builder.add_conditional_edges(
    "chatbot",
    tools_condition
)
builder.add_edge(
    "tools",
    "chatbot"
)


# ---------------------------------------------------
# Memory
# ---------------------------------------------------

memory = MemorySaver()


# ---------------------------------------------------
# Compile
# ---------------------------------------------------
graph = builder.compile(
    checkpointer=memory,
)

