"""
Retriever Module
"""


def retrieve_documents(
    vectorstore,
    query,
    k=4
):
    """
    Retrieve top-k relevant chunks.
    """

    docs = vectorstore.similarity_search(
        query,
        k=k
    )

    return docs


def build_context(
    docs
):
    """
    Convert retrieved docs into context.
    """

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


def extract_sources(
    docs
):
    """
    Extract page numbers.
    """

    pages = sorted(
        set(
            doc.metadata["page"] + 1
            for doc in docs
        )
    )

    return pages