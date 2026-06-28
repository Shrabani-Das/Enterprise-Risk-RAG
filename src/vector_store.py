"""
FAISS Vector Store Module
"""

from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

VECTOR_DB_PATH = PROJECT_ROOT / "vectorstore" / "faiss_index"


# ==========================================================
# Embedding Model
# ==========================================================

def load_embedding_function():
    """
    Load HuggingFace embedding model.
    """

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# ==========================================================
# Create Vector Store
# ==========================================================

def create_vector_store(chunks, embedding_function=None):
    """
    Create FAISS vector store from LangChain Documents.
    """

    if embedding_function is None:
        embedding_function = load_embedding_function()

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_function
    )

    return vectorstore


# ==========================================================
# Save Vector Store
# ==========================================================

def save_vector_store(vectorstore):
    """
    Save FAISS index.
    """

    VECTOR_DB_PATH.mkdir(parents=True, exist_ok=True)

    vectorstore.save_local(str(VECTOR_DB_PATH))

    print(f"\n✅ Vector Store Saved Successfully")
    print(f"Location : {VECTOR_DB_PATH}")


# ==========================================================
# Load Vector Store
# ==========================================================

def load_vector_store():
    """
    Load FAISS vector database.
    """

    embedding_function = load_embedding_function()


    vectorstore = FAISS.load_local(
        str(VECTOR_DB_PATH),
        embedding_function,
        allow_dangerous_deserialization=True
    )

    return vectorstore