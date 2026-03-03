from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_sentiment(text):

    prompt = f"""
    Analyze the sentiment of this travel review.
    Classify as Positive, Negative, or Neutral.
    Also give a short explanation.

    Review:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
