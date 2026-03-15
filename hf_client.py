import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise Exception("HF_TOKEN not found. Please add it to .env file")
print("HF TOKEN LOADED:", HF_TOKEN)   # debugging

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def query_hf_model(api_url, payload, retries=3):
    """
    Generic function to call HuggingFace Inference API
    with retry support for model cold start.
    """

    # Convert old HuggingFace endpoint to new router endpoint
    router_url = api_url.replace(
        "https://api-inference.huggingface.co/models/",
        "https://router.huggingface.co/hf-inference/models/"
    )

    for attempt in range(retries):

        try:
            response = requests.post(
                router_url,
                headers=headers,
                json=payload,
                timeout=60
            )

            # Successful response
            if response.status_code == 200:
                return response.json()

            # Model loading (cold start)
            if response.status_code == 503:
                print("Model loading... waiting 15 seconds")
                time.sleep(15)
                continue

            # Other API errors
            raise Exception(f"HuggingFace API Error: {response.text}")

        except requests.exceptions.RequestException as e:
            print("Request failed:", str(e))
            time.sleep(5)

    raise Exception("Model loading timeout. Try again later.")