import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")




headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query_hf_model(api_url, payload, retries=3):
    for attempt in range(retries):
        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()

        # Model cold start handling
        if response.status_code == 503:
            time.sleep(15)
            continue

        raise Exception(f"HuggingFace API Error: {response.text}")

    raise Exception("Model loading timeout. Try again.")
