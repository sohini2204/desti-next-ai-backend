import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# ==========================================
# Load SBERT Model (Loaded Once Globally)
# ==========================================
model = SentenceTransformer("all-MiniLM-L6-v2")


# ==========================================
# Generate Embeddings
# ==========================================
def generate_embeddings(text_list):
    """
    Generate embeddings for a list of text inputs.
    """
    embeddings = model.encode(text_list)
    return np.array(embeddings).astype("float32")


# ==========================================
# Load Destination Dataset
# ==========================================
def load_destination_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "data", "CLEAN_Destinations.csv")

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    # Create combined text field
    df["text_data"] = (
        df["destination"].astype(str) + " " +
        df["state"].astype(str) + " " +
        df["category"].astype(str)
    )

    return df
