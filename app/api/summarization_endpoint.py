from fastapi import APIRouter, HTTPException
from app.schemas.summarization_schema import SummarizationRequest, SummarizationResponse
from app.services.summarization_service import summarize_text

router = APIRouter()

@router.post("/summarize", response_model=SummarizationResponse)
async def text_summarization(request: SummarizationRequest):
    """
    Endpoint for text summarization.
    """
    pass