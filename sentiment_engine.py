from hf_client import query_hf_model

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

def analyze_sentiment(text):
    """
    Analyze sentiment of a travel review.
    Returns a classification like 'POSITIVE' or 'NEGATIVE'.
    """
    result = query_hf_model(API_URL, {"inputs": text})
    return result
  
