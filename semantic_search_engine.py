import faiss
import numpy as np
from embedding_engine import generate_embeddings, load_destination_data


def build_faiss_index():
    df = load_destination_data()
    embeddings = generate_embeddings(df["text_data"].tolist())

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return df, index


def semantic_search(query, k=5):
    df, index = build_faiss_index()

    query_vector = generate_embeddings([query])
    distances, indices = index.search(query_vector, k)

    return df.iloc[indices[0]][["destination", "state", "category"]]
