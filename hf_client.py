import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query_hf_model(api_url, payload):
    response = requests.post(
        api_url,
        headers=headers,
        json=payload
    )
    return response.json()
