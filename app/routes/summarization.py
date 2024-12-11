from fastapi import APIRouter, HTTPException
from app.models.summarization import summarize_text

router = APIRouter()

@router.post("/summarize")
async def text_summarization(payload: dict):
    text = payload.get("text", "")
    
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    try:
        result = summarize_text(text)
        return {"summary": result}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")