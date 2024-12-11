from fastapi.testclient import TestClient
from app.main import app
from app.schemas.summarization_schema import SummarizationResponse
from unittest.mock import patch

client = TestClient(app)

def test_summarization_long_text():
    """Test summarization with long AGI text"""
    test_text = """The concept of Artificial General Intelligence (AGI)..."""
    expected_summary = """Artificial General Intelligence (AGI) aims to replicate..."""
    
    with patch('app.api.summarization_endpoint.summarize_text', return_value=expected_summary):
        response = client.post(
            "/summarize",
            json={"text": test_text}
        )
        assert response.status_code == 200
        
        response_data = SummarizationResponse(**response.json())
        assert response_data.summary == expected_summary
        assert response_data.original_length == len(test_text)
        assert response_data.summary_length == len(expected_summary)

def test_summarization_empty_text():
    response = client.post(
        "/summarize",
        json={"text": ""}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Input text cannot be empty"

def test_summarization_invalid_request():
    response = client.post(
        "/summarize",
        json={}
    )
    assert response.status_code == 422  # FastAPI validation error