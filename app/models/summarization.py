import requests
from app.config import HUGGINGFACE_API_BASE, SUMMARIZATION_MODEL, API_HEADERS

def summarize_text(text: str) -> str:
    """
    Makes a request to Hugging Face API to summarize text.
    
    Args:
        text (str): The text to be summarized
        
    Returns:
        str: Summarized text
        
    Raises:
        ValueError: If text is empty
        Exception: If API request fails
    """
    if not text.strip():
        raise ValueError("Input text cannot be empty")
        
    try:
        # Construct API URL for the summarization model
        api_url = f"{HUGGINGFACE_API_BASE}/{SUMMARIZATION_MODEL}"
        
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
        
        # Extract summary from response
        if isinstance(result, list) and len(result) > 0:
            return result[0]["summary_text"]
        else:
            raise Exception("Invalid response format from Hugging Face API")
            
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to connect to Hugging Face API: {str(e)}")
    except Exception as e:
        raise Exception(f"Summarization failed: {str(e)}")
