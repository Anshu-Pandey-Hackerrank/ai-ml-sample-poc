from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.models.sentiment import analyze_sentiment

router = APIRouter()

# Define request model
class SentimentRequest(BaseModel):
    text: str

@router.post("/sentiment")
async def sentiment_analysis(request: SentimentRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text is required")
    try:
        result = analyze_sentiment(request.text)
        return {
            "text": request.text,
            "emotion": result["label"],
            "confidence": result["score"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))