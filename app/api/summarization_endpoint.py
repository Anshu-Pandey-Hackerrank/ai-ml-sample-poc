from fastapi import APIRouter, HTTPException
from app.schemas.summarization_schema import SummarizationRequest, SummarizationResponse
from app.services.summarization_service import summarize_text

router = APIRouter()

@router.post("/summarize", response_model=SummarizationResponse)
async def text_summarization(request: SummarizationRequest):
    try:
        summary = summarize_text(request.text)
        return SummarizationResponse(
            summary=summary,
            original_length=len(request.text),
            summary_length=len(summary)
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Internal Server Error: {str(e)}"
        )