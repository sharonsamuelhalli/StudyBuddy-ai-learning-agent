"""
Configuration module for StudyBuddy AI Learning Agent.

Responsibilities:
- Load environment variables from .env
- Store API keys
- Store Gemini model configuration
- Store application-wide constants
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("API KEY:", GEMINI_API_KEY)
GEMINI_MODEL = "gemini-2.5-flash"

# Model Settings
TEMPERATURE = 0.3
MAX_OUTPUT_TOKENS = 2048


def validate_config():
    """
    Validate that the required configuration is available.
    """

    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY not found. Please add it to your .env file."
        )