"""
Base Agent Class
Responsibility:
- Maintain shared client instance of Gemini API.
- Provide general utility methods for reading external prompt files and running LLM generate tasks.
"""

from google import genai
from src.config import GEMINI_API_KEY, GEMINI_MODEL

class BaseAgent:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or GEMINI_API_KEY
        # When google-genai SDK is used:
        # self.client = genai.Client(api_key=self.api_key)
        self.model = GEMINI_MODEL
        
    def _read_prompt_template(self, template_name: str) -> str:
        """Helper to read prompt from templates folder."""
        # Implementation to resolve file path under src/prompts/ and read string
        return ""
