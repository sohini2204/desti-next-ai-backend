from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def recommend_destination(user_interest):

    prompt = f"""
    A user is interested in: {user_interest}.
    Recommend 5 travel destinations.
    Return them as a simple list with destination name and category.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
