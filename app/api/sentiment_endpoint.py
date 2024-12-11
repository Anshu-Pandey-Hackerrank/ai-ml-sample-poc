from fastapi import APIRouter, HTTPException
from app.schemas.sentiment_schema import SentimentRequest, SentimentResponse
from app.services.sentiment_service import analyze_sentiment

router = APIRouter()

@router.post("/sentiment", response_model=SentimentResponse)
async def sentiment_analysis(request: SentimentRequest):
    try:
        result = analyze_sentiment(request.text)
        return SentimentResponse(
            text=request.text,
            emotion=result["label"],
            confidence=result["score"]
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Internal Server Error: {str(e)}"
        )