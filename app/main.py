from fastapi import FastAPI
from app.routes import sentiment, summarization

app = FastAPI(
    title="AI/ML Text Analysis API",
    description="An API for sentiment analysis and text summarization using Hugging Face models.",
    version="1.0.0"
)

# Welcome route
@app.get("/")
async def welcome():
    return {
        "message": "Welcome to the AI/ML Text Analysis API",
        "available_endpoints": {
            "sentiment_analysis": "/sentiment",
            "text_summarization": "/summarize"
        }
    }

# Include routes
app.include_router(sentiment.router, prefix="", tags=["Sentiment Analysis"])
app.include_router(summarization.router, prefix="", tags=["Text Summarization"])
