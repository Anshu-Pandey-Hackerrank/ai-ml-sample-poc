from fastapi import FastAPI
from app.api import sentiment_endpoint, summarization_endpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="AI/ML Text Analysis API",
    description="An API for sentiment analysis and text summarization using Hugging Face Inference API.",
    version="1.0.0"
)

# Welcome route
@app.get("/")
async def welcome():
    return {
        "message": "Welcome to the Content Text Analysis API",
        "available_endpoints": {
            "sentiment_analysis": "/sentiment",
            "text_summarization": "/summarize"
        }
    }

# Include routes
app.include_router(sentiment_endpoint.router, tags=["Sentiment Analysis"])
app.include_router(summarization_endpoint.router, tags=["Text Summarization"])
