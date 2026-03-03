import numpy as np
from scipy.spatial.distance import cdist
from embedding_engine import generate_embeddings
from data_loader import load_destination_data

def semantic_search(query, k=5):
    """
    Perform semantic search over the destinations dataset
    using HuggingFace embeddings and cosine similarity.

    Returns top-k most similar destinations.
    """

    # Load dataset
    df = load_destination_data()

    # Compute embeddings for all destinations
    doc_embeddings = generate_embeddings(df["text_data"].tolist())

    # Compute embedding for the query
    query_embedding = generate_embeddings([query])[0]

    # Cosine similarity
    similarities = 1 - cdist([query_embedding], doc_embeddings, metric="cosine")[0]

    # Add similarity scores
    df["similarity"] = similarities

    # Return top-k results
    return df.sort_values("similarity", ascending=False).head(k)
