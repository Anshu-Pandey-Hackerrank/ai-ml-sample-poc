from fastapi.testclient import TestClient
from app.main import app
from app.schemas.sentiment_schema import SentimentResponse
from unittest.mock import patch

client = TestClient(app)

def test_sentiment_analysis_disapproval():
    """Test sentiment analysis with disapproval emotion"""
    test_text = "The product seems bad with a dent on it. Although it is not noticible"
    
    mock_result = {
        "label": "disapproval",
        "score": 0.3766115605831146
    }
    
    with patch('app.api.sentiment_endpoint.analyze_sentiment', return_value=mock_result):
        response = client.post(
            "/sentiment",
            json={"text": test_text}
        )
        assert response.status_code == 200
        
        response_data = SentimentResponse(**response.json())
        assert response_data.text == test_text
        assert response_data.emotion == "disapproval"
        assert response_data.confidence == 0.3766115605831146

def test_sentiment_analysis_positive():
    """Test sentiment analysis with positive emotion"""
    test_text = "I love this product! It's amazing and works perfectly."
    
    mock_result = {
        "label": "approval",
        "score": 0.9876543
    }
    
    with patch('app.api.sentiment_endpoint.analyze_sentiment', return_value=mock_result):
        response = client.post(
            "/sentiment",
            json={"text": test_text}
        )
        assert response.status_code == 200
        
        response_data = SentimentResponse(**response.json())
        assert response_data.text == test_text
        assert response_data.emotion == "approval"
        assert response_data.confidence == 0.9876543

def test_sentiment_analysis_empty_text():
    response = client.post(
        "/sentiment",
        json={"text": ""}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Input text cannot be empty"

