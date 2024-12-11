from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarization():
    long_text = """
    New York (CNN) When Liana Barrientos was 23 years old, she got married in Westchester County, New York. 
    A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
    Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, 
    sometimes only within two weeks of each other. In 2010, she married once more, this time in the Bronx.
    """
    
    response = client.post(
        "/summarize",
        json={"text": long_text}
    )
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert isinstance(data["summary"], str)
    assert len(data["summary"]) < len(long_text)

def test_summarization_empty_text():
    response = client.post(
        "/summarize",
        json={"text": ""}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Text is required"

def test_summarization_invalid_request():
    response = client.post(
        "/summarize",
        json={}
    )
    assert response.status_code == 400