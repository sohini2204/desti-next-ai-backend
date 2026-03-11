from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import traceback
import pandas as pd

from content_engine import (
    generate_travel_story,
    generate_promotional_content,
    generate_social_media_posts,
    generate_reviews
)

from recommendation_engine import recommend_destination
from sentiment_engine import analyze_sentiment
from semantic_search_engine import semantic_search
from rag_engine import rag_chatbot, generate_ai_response

from multilingual_engine import multilingual_pipeline
from dashboard import revenue_chart, seasonal_chart

app = FastAPI(title="Desti Next AI Backend")

# =============================
# CORS CONFIGURATION
# =============================
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================
# Request Models
# =============================
class TextRequest(BaseModel):
    text: str

class InterestRequest(BaseModel):
    interest: str


# =============================
# Multilingual Response Function
# =============================
def get_response(user_input):

    response = multilingual_pipeline(
        user_input,
        generate_ai_response
    )

    return response


# =============================
# Helper function
# =============================
def safe_execute(func, *args, **kwargs):
    try:
        return {"result": func(*args, **kwargs)}
    except Exception as e:
        print(f"Error in {func.__name__}:", str(e))
        traceback.print_exc()
        return {"error": "Internal server error"}


# =============================
# API Endpoints
# =============================

@app.post("/generate-story")
def story(data: TextRequest):
    return safe_execute(generate_travel_story, data.text)


@app.post("/generate-promo")
def promo(data: TextRequest):
    return safe_execute(generate_promotional_content, data.text)


@app.post("/generate-social")
def social(data: TextRequest):
    return safe_execute(generate_social_media_posts, data.text)


@app.post("/recommend")
def recommend(data: InterestRequest):
    return safe_execute(recommend_destination, data.interest)


@app.post("/search")
def search(data: TextRequest):

    result = safe_execute(semantic_search, data.text)

    if "result" in result and hasattr(result["result"], "to_dict"):
        result["result"] = result["result"].to_dict(orient="records")

    return result


@app.post("/sentiment")
def sentiment(data: TextRequest):
    return safe_execute(analyze_sentiment, data.text)


# =============================
# Multilingual Chat Endpoint
# =============================
@app.post("/chat")
def chat(data: TextRequest):
    return safe_execute(get_response, data.text)


@app.post("/reviews")
def reviews(data: TextRequest):
    return safe_execute(generate_reviews, data.text)


# =============================
# Destination List
# =============================

destinations_df = pd.read_csv("data/CLEAN_Destinations.csv")

@app.get("/destinations")
def get_destinations():

    places = destinations_df["destination"].dropna().unique().tolist()

    return {"destinations": places}


# =============================
# Dashboard APIs
# =============================

@app.get("/dashboard/revenue")
def get_revenue_chart():
    fig = revenue_chart()
    return fig


@app.get("/dashboard/seasonal")
def get_seasonal_chart():
    fig = seasonal_chart()
    return fig


# =============================
# Root Health Check
# =============================

@app.get("/")
def root():
    return {"status": "Backend is running!"}