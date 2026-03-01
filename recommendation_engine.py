import pandas as pd
from sklearn.neighbors import NearestNeighbors
from embedding_engine import generate_embeddings

def recommend_destination(user_interest):
    df = pd.read_csv("data/CLEAN_Destinations.csv")

    df["combined"] = df["category"] + " " + df["description"]

    embeddings = generate_embeddings(df["combined"].tolist())

    knn = NearestNeighbors(n_neighbors=5, metric="cosine")
    knn.fit(embeddings)

    user_embedding = generate_embeddings([user_interest])
    distances, indices = knn.kneighbors(user_embedding)

    return df.iloc[indices[0]][["destination_name", "category"]]