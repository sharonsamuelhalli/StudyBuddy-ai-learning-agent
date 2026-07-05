"""
Base Agent for StudyBuddy AI Learning Agent.

Responsibilities:
- Initialize Gemini client.
- Load prompt templates.
- Send prompts to Gemini.
"""

from google import genai
from src.config import GEMINI_API_KEY, GEMINI_MODEL


class BaseAgent:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = GEMINI_MODEL

    def load_prompt(self, prompt_path: str) -> str:
        """Load a prompt template from a text file."""
        with open(prompt_path, "r", encoding="utf-8") as file:
            return file.read()

    def generate_response(self, prompt: str) -> str:
        """Send a prompt to Gemini and return the response."""
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text