from pydantic import BaseModel

class SummarizationRequest(BaseModel):
    text: str

class SummarizationResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int
