from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer


def load_embedding_model(model_name="all-MiniLM-L6-v2"):
    return SentenceTransformer(model_name)


def create_embeddings(model, texts):
    """
    Generate embeddings from either:
    - list[str]
    - list[Document]
    """

    if len(texts) == 0:
        raise ValueError("Input list is empty.")

    # Convert Documents to strings automatically
    if isinstance(texts[0], Document):
        texts = [doc.page_content for doc in texts]

    return model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True
    )