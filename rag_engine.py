from hf_client import query_hf_model

# HuggingFace text generation model
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

def rag_chatbot(query):
    """
    RAG-style chatbot response for travel questions using HF model.
    """
    prompt = f"Answer this travel question clearly and professionally:\n\n{query}"
    result = query_hf_model(API_URL, {"inputs": prompt})
    return result[0]["generated_text"]
