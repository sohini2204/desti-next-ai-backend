import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import ollama

# Load dataset
df = pd.read_csv("data/CLEAN_Destinations.csv")
destinations = df["destination"].dropna().tolist()

# Load embedding model ONLY ONCE
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings once
embeddings = model.encode(destinations)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


def chatbot_response(query):

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, 5)

    relevant_places = [destinations[i] for i in indices[0]]

    context = ", ".join(relevant_places)

    prompt = f"""
You are **DestiNext Guide**, an AI travel assistant for the DestiNext platform.

Your role is to help users discover destinations, tourism insights, and travel ideas.

Relevant destinations:
{context}

User question:
{query}

Answer briefly in 2-3 sentences.
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.message.content