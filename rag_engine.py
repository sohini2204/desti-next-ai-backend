import os
import faiss
import numpy as np
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from embedding_engine import generate_embeddings, load_destination_data

# ==========================================
# Load LLM Once (Global)
# ==========================================
tokenizer = AutoTokenizer.from_pretrained("gpt2")
llm = AutoModelForCausalLM.from_pretrained("gpt2")

# ==========================================
# Build FAISS Index Once
# ==========================================
df = load_destination_data()

documents = df["text_data"].tolist()
embeddings = generate_embeddings(documents)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


# ==========================================
# RAG Chatbot Function
# ==========================================
def rag_chatbot(query, k=3):

    # Encode query
    query_vector = generate_embeddings([query])

    # Retrieve similar docs
    distances, indices = index.search(query_vector, k)

    context = " ".join(df.iloc[indices[0]]["text_data"].tolist())

    prompt = f"""
    You are an intelligent tourism assistant.
    Use the context below to answer clearly and concisely.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    inputs = tokenizer(prompt, return_tensors="pt")

    output = llm.generate(
        **inputs,
        max_length=300,
        temperature=0.7,
        top_k=50,
        do_sample=True
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Remove prompt from output
    final_answer = response.split("Answer:")[-1].strip()

    return final_answer
