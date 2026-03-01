from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_travel_story(destination):
    prompt = f"Write an engaging travel story about {destination} highlighting culture, food, and experiences."
    result = generator(prompt, max_length=300, temperature=0.9)
    return result[0]["generated_text"]


def generate_promotional_content(destination):
    prompt = f"Write a tourism marketing blog for {destination} with attractions, best time to visit and tips."
    result = generator(prompt, max_length=350)
    return result[0]["generated_text"]


def generate_social_media_posts(destination):
    prompt = f"Create 5 Instagram captions with hashtags for promoting {destination}."
    result = generator(prompt, max_length=200)
    return result[0]["generated_text"]
