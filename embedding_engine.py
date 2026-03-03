import os
import pandas as pd
import numpy as np
from openai import OpenAI

# ==========================================
# OpenAI Client
# ==========================================
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ==========================================
# Generate Embeddings (OpenAI)
# ==========================================
def generate_embeddings(text_list):
    """
    Generate embeddings using OpenAI API.
    """
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text_list
    )

    embeddings = [item.embedding for item in response.data]
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
