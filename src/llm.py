import os

import streamlit as st

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


def load_llm():

    api_key = st.secrets.get(
        "GROQ_API_KEY",
        os.getenv("GROQ_API_KEY")
    )

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=api_key
    )

    return llm



def build_prompt():

    return ChatPromptTemplate.from_template(
        """
You are an expert Basel III regulatory assistant.

Rules

1. Answer ONLY using the provided context.

2. Never use outside knowledge.

3. If the answer is unavailable reply:

"I don't have enough information in the provided Basel document."

Context

{context}

Question

{question}

Answer
"""
    )


def generate_answer(
    llm,
    prompt,
    context,
    question
):

    formatted_prompt = prompt.format(
        context=context,
        question=question
    )

    response = llm.invoke(formatted_prompt)

    return response.content