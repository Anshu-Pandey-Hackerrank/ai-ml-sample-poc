import requests
from app.config import HUGGINGFACE_API_BASE, SENTIMENT_MODEL, API_HEADERS

def analyze_sentiment(text: str) -> dict:
    """
    Makes a request to Hugging Face API for sentiment analysis.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: Contains emotion label and confidence score
        
    Raises:
        ValueError: If text is empty
        Exception: If API request fails
    """
    if not text.strip():
        raise ValueError("Input text cannot be empty")
        
    try:
        # Construct API URL for the sentiment model
        api_url = f"{HUGGINGFACE_API_BASE}/{SENTIMENT_MODEL}"
        
        # Make request to Hugging Face API
        response = requests.post(
            api_url,
            headers=API_HEADERS,
            json={"inputs": text}
        )
        
        # Check response status
        if response.status_code != 200:
            raise Exception(f"Hugging Face API request failed: {response.status_code}")
            
        # Parse response
        result = response.json()
        
        # Extract sentiment from response
        if isinstance(result, list) and len(result) > 0:
            return {
                "label": result[0][0]["label"],
                "score": result[0][0]["score"]
            }
        else:
            raise Exception("Invalid response format from Hugging Face API")
            
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to connect to Hugging Face API: {str(e)}")
    except Exception as e:
        raise Exception(f"Sentiment analysis failed: {str(e)}")
