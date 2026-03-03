from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_travel_story(destination):
    prompt = f"Write an engaging travel story about {destination} highlighting culture, food, and experiences."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        max_tokens=400
    )
    
    return response.choices[0].message.content


def generate_promotional_content(destination):
    prompt = f"Write a tourism marketing blog for {destination} with attractions, best time to visit and tips."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=450
    )
    
    return response.choices[0].message.content


def generate_social_media_posts(destination):
    prompt = f"Create 5 Instagram captions with hashtags for promoting {destination}."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=300
    )
    
    return response.choices[0].message.content
