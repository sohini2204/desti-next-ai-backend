from fastapi import FastAPI
from pydantic import BaseModel

from content_engine import (
    generate_travel_story,
    generate_promotional_content,
    generate_social_media_posts
)
from recommendation_engine import recommend_destination
from sentiment_engine import analyze_sentiment
from semantic_search_engine import semantic_search
from rag_engine import rag_chatbot
from multilingual_engine import translate_text
from dashboard import revenue_chart, seasonal_chart

app = FastAPI()

# =============================
# Request Models
# =============================

class TextRequest(BaseModel):
    text: str

class InterestRequest(BaseModel):
    interest: str


# =============================
# API Endpoints
# =============================

@app.post("/generate-story")
def story(data: TextRequest):
    return {"result": generate_travel_story(data.text)}


@app.post("/generate-promo")
def promo(data: TextRequest):
    return {"result": generate_promotional_content(data.text)}


@app.post("/generate-social")
def social(data: TextRequest):
    return {"result": generate_social_media_posts(data.text)}


@app.post("/recommend")
def recommend(data: InterestRequest):
    result = recommend_destination(data.interest)
    return {"result": result.to_dict(orient="records")}


@app.post("/search")
def search(data: TextRequest):
    result = semantic_search(data.text)
    return {"result": result.to_dict(orient="records")}


@app.post("/sentiment")
def sentiment(data: TextRequest):
    return {"result": analyze_sentiment(data.text)}


@app.post("/chat")
def chat(data: TextRequest):
    return {"result": rag_chatbot(data.text)}


@app.post("/translate")
def translate(data: TextRequest):
    return {"result": translate_text(data.text)}