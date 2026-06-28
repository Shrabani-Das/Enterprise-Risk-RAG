from src.vector_store import load_vector_store
from src.retriever import retrieve_documents, build_context, extract_sources
from src.llm import load_llm, build_prompt, generate_answer


import streamlit as st

@st.cache_resource
def get_vectorstore():
    return load_vector_store()

@st.cache_resource
def get_llm():
    return load_llm()

# Load once
vectorstore = get_vectorstore()
llm = get_llm()

prompt = build_prompt()


def ask(question):

    docs = retrieve_documents(
        vectorstore,
        question,
        k=4
    )

    context = build_context(docs)

    answer = generate_answer(
        llm,
        prompt,
        context,
        question
    )

    sources = extract_sources(docs)

    return {
        "answer": answer,
        "sources": sources
    }