import os
import pandas as pd

def load_destination_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "data", "CLEAN_Destinations.csv")

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    df["text_data"] = (
        df["destination"].astype(str) + " " +
        df["state"].astype(str) + " " +
        df["category"].astype(str)
    )

    return df
