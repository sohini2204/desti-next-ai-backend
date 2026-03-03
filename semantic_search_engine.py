from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def semantic_search(query, k=5):

    prompt = f"""
    A user searched for: {query}.
    Suggest {k} relevant travel destinations with state and category.
    Return as a clear list.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
