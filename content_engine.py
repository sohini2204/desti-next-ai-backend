from hf_client import query_hf_model

# HuggingFace text generation model
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

def generate_travel_story(destination):
    """
    Generate an engaging travel story about a destination.
    """
    prompt = f"Write an engaging travel story about {destination} highlighting culture, food, and experiences."
    result = query_hf_model(API_URL, {"inputs": prompt})
    return result[0]["generated_text"]


def generate_promotional_content(destination):
    """
    Generate a tourism marketing blog for a destination.
    """
    prompt = f"Write a tourism marketing blog for {destination} with attractions, best time to visit and tips."
    result = query_hf_model(API_URL, {"inputs": prompt})
    return result[0]["generated_text"]


def generate_social_media_posts(destination):
    """
    Create 5 Instagram captions with hashtags for promoting a destination.
    """
    prompt = f"Create 5 Instagram captions with hashtags for promoting {destination}."
    result = query_hf_model(API_URL, {"inputs": prompt})
    return result[0]["generated_text"]
