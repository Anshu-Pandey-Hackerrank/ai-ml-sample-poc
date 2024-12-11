from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sentiment_analysis_positive():
    response = client.post(
        "/sentiment",
        json={"text": "I love this product! It's amazing and works perfectly."}
    )
    assert response.status_code == 200
    data = response.json()
    assert "emotion" in data
    assert "confidence" in data
    assert "text" in data
    assert isinstance(data["confidence"], float)
    assert 0 <= data["confidence"] <= 1

def test_sentiment_analysis_empty_text():
    response = client.post(
        "/sentiment",
        json={"text": ""}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Text is required"

def test_sentiment_analysis_invalid_request():
    response = client.post(
        "/sentiment",
        json={}
    )
    assert response.status_code == 422  # Validation Error