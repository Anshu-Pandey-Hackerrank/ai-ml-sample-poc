from fastapi import APIRouter, HTTPException
from app.schemas.sentiment_schema import SentimentRequest, SentimentResponse
from app.services.sentiment_service import analyze_sentiment

router = APIRouter()

@router.post("/sentiment", response_model=SentimentResponse)
async def sentiment_analysis(request: SentimentRequest):
    """
    Endpoint for sentiment analysis.
    """
    pass