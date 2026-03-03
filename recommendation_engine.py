from hf_client import query_hf_model

# HuggingFace text generation model
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

def recommend_destination(user_interest):
    """
    Recommend 5 travel destinations based on user interest.
    Returns them as a simple list with destination name and category.
    """
    prompt = (
        f"A user is interested in: {user_interest}.\n"
        "Recommend 5 travel destinations.\n"
        "Return them as a clear, numbered list with destination name and category."
    )

    result = query_hf_model(API_URL, {"inputs": prompt})
    return result[0]["generated_text"]
