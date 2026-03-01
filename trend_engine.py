import pandas as pd
from sklearn.cluster import KMeans
from embedding_engine import generate_embeddings

def detect_topics():
    df = pd.read_csv("data/CLEAN_Source_Country.csv")

    embeddings = generate_embeddings(df["review"].tolist())

    kmeans = KMeans(n_clusters=5, random_state=42)
    df["topic"] = kmeans.fit_predict(embeddings)

    return df[["review", "topic"]]
