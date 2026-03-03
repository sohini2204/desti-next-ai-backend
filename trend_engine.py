import pandas as pd
from hf_client import query_hf_model

# HuggingFace text generation model
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

def detect_topics(n_samples=20):
    """
    Detect major themes/topics from travel reviews.
    Returns a string listing reviews and their assigned topic.
    """
    df = pd.read_csv("data/CLEAN_Source_Country.csv")
    reviews = df["review"].tolist()[:n_samples]

    prompt = (
        "Group the following travel reviews into 5 major themes.\n"
        "Return output as:\nReview: <text>\nTopic: <theme name>\n\n"
        f"Reviews:\n{reviews}"
    )

    result = query_hf_model(API_URL, {"inputs": prompt})
    return result[0]["generated_text"]
