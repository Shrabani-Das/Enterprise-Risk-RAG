"""
Document Loader Module

Loads PDF documents using LangChain's PyPDFLoader.
"""

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path: str):
    """
    Load a PDF document.

    Parameters
    ----------
    pdf_path : str
        Path to PDF.

    Returns
    -------
    list
        List of LangChain Document objects.
    """

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents