"""
Configuration module for StudyBuddy AI Learning Agent
Responsibility:
- Load variables from .env
- Centralize API Keys, model designations, and hyperparameters
"""

import os
from dotenv import load_dotenv

# Load local environment variables
load_dotenv()

# Gemini Config
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"  # Highly efficient, fast model for textual analysis & MVP
