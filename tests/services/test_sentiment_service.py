import pytest
from unittest.mock import patch, Mock
from app.services.summarization_service import summarize_text
import requests

def test_summarize_text_success():
    """Test successful text summarization"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"summary_text": "Brief summary"}]
    
    with patch('requests.post', return_value=mock_response):
        result = summarize_text("Long text to summarize")
        assert result == "Brief summary"

def test_summarize_text_empty_text():
    """Test summarization with empty text"""
    with pytest.raises(ValueError) as exc_info:
        summarize_text("")
    assert str(exc_info.value) == "Input text cannot be empty"

def test_summarize_text_api_error():
    """Test handling of API errors"""
    mock_response = Mock()
    mock_response.status_code = 500
    
    with patch('requests.post', return_value=mock_response):
        with pytest.raises(Exception) as exc_info:
            summarize_text("Some text")
        assert "Hugging Face API request failed: 500" in str(exc_info.value)

def test_summarize_text_connection_error():
    """Test handling of connection errors"""
    with patch('requests.post', side_effect=requests.exceptions.RequestException("Connection failed")):
        with pytest.raises(Exception) as exc_info:
            summarize_text("Some text")
        assert str(exc_info.value) == "Failed to connect to Hugging Face API: Connection failed"
