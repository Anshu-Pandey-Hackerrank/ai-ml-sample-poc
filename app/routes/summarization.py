from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.summarization import summarize_text

router = APIRouter()

# Define request model
class SummarizationRequest(BaseModel):
    text: str

@router.post("/summarize")
async def text_summarization(request: SummarizationRequest):
    """
    FastAPI endpoint to handle text summarization requests.
    
    Args:
        request (SummarizationRequest): Request body containing text to summarize
        
    Returns:
        dict: Contains the summarized text
        
    Raises:
        HTTPException: 400 for invalid input, 500 for server errors
    """
    try:
        # Get summary from Hugging Face API
        summary = summarize_text(request.text)
        
        # Return response
        return {
            "summary": summary,
            "original_length": len(request.text),
            "summary_length": len(summary)
        }
        
    except ValueError as ve:
        # Handle validation errors (empty text, etc.)
        raise HTTPException(
            status_code=400,
            detail=str(ve)
        )
    except Exception as e:
        # Handle all other errors (API failures, etc.)
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error: {str(e)}"
        )