from os import getenv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
HUGGINGFACE_API_BASE = ""
HUGGINGFACE_TOKEN = ""

# Model Configuration
SUMMARIZATION_MODEL = "facebook/bart-large-cnn"
SENTIMENT_MODEL = "SamLowe/roberta-base-go_emotions"

# Headers for API requests
API_HEADERS = {}