from openai import OpenAI
import os
import pandas as pd

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def detect_topics():
    df = pd.read_csv("data/CLEAN_Source_Country.csv")

    reviews = df["review"].tolist()

    prompt = f"""
    Group the following travel reviews into 5 major themes.
    Return output as:
    Review: <text>
    Topic: <theme name>

    Reviews:
    {reviews[:20]}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
