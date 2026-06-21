"""
Text Chunking Module

This module contains utility functions for splitting LangChain
Document objects into smaller chunks suitable for Retrieval-
Augmented Generation (RAG).
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(
    documents,
    chunk_size=1000,
    chunk_overlap=200
):

    if not documents:
        raise ValueError("Document list is empty.")

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be smaller than chunk_size."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    return splitter.split_documents(documents)