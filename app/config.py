from os import getenv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
HUGGINGFACE_API_BASE = "https://api-inference.huggingface.co/models"
HUGGINGFACE_TOKEN = getenv("HUGGINGFACE_API_TOKEN")

# Model Configuration
SUMMARIZATION_MODEL = "facebook/bart-large-cnn"
SENTIMENT_MODEL = "SamLowe/roberta-base-go_emotions"

# Headers for API requests
API_HEADERS = {
    "Authorization": f"Bearer {HUGGINGFACE_TOKEN}",
    "Content-Type": "application/json"
}