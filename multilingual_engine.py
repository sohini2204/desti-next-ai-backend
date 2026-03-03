from hf_client import query_hf_model

# HuggingFace translation model
API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-hi"

def translate_text(text):
    """
    Translate English text to Hindi using HF model.
    """
    result = query_hf_model(API_URL, {"inputs": text})
    return result[0]["translation_text"]
