import numpy as np
from hf_client import query_hf_model

# HuggingFace Embedding Model
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"


# ==========================================
# Generate Embeddings (HuggingFace)
# ==========================================
def generate_embeddings(text_list):
    """
    Generate embeddings using HuggingFace Inference API.
    """

    embeddings = []

    for text in text_list:
        result = query_hf_model(API_URL, {"inputs": text})

        # HF returns a list of floats
        if isinstance(result, list):
            embeddings.append(result)
        else:
            raise ValueError("Unexpected embedding response format from HF API")

    return np.array(embeddings, dtype="float32")
