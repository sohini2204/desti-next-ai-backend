from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rag_chatbot(query, k=3):

    prompt = f"""
    You are an intelligent tourism assistant.

    A user asked: {query}

    Provide a helpful, clear, and tourism-focused answer.
    If relevant, suggest destinations, tips, or travel insights.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
