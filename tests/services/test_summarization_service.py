import pytest
from unittest.mock import patch, Mock
from app.services.summarization_service import summarize_text
import requests

@pytest.fixture
def mock_successful_response():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"summary_text": "Liana Barrientos married multiple times without divorcing."}]
    return mock_response

def test_summarize_text_success(mock_successful_response):
    """Test successful text summarization"""
    with patch('requests.post', return_value=mock_successful_response):
        result = summarize_text("Long text about marriages")
        assert isinstance(result, str)
        assert result == "Liana Barrientos married multiple times without divorcing."

def test_summarize_text_empty_text():
    """Test empty text validation"""
    with pytest.raises(ValueError, match="Input text cannot be empty"):
        summarize_text("")

def test_summarize_text_whitespace_text():
    """Test whitespace-only text validation"""
    with pytest.raises(ValueError, match="Input text cannot be empty"):
        summarize_text("   \n\t   ")

def test_summarize_text_api_error():
    """Test API error handling"""
    mock_response = Mock()
    mock_response.status_code = 500
    
    with patch('requests.post', return_value=mock_response):
        with pytest.raises(Exception, match="Hugging Face API request failed: 500"):
            summarize_text("Some text")

def test_summarize_text_invalid_response():
    """Test invalid API response handling"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}
    
    with patch('requests.post', return_value=mock_response):
        with pytest.raises(Exception, match="Invalid response format"):
            summarize_text("Some text")

def test_summarize_text_connection_error():
    """Test connection error handling"""
    with patch('requests.post', side_effect=requests.exceptions.RequestException("Connection failed")):
        with pytest.raises(Exception) as exc_info:
            summarize_text("Some text")
        assert str(exc_info.value) == "Failed to connect to Hugging Face API: Connection failed"
