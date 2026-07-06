"""
Base Agent for StudyBuddy AI Learning Agent.

Responsibilities:
- Initialize Gemini client.
- Load prompt templates.
- Send prompts to Gemini.
"""
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

class BaseAgent:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        print("API KEY:", os.getenv("GEMINI_API_KEY"))

    def load_prompt(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def generate_response(self, prompt):
        try:
            response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
            return response.text

        except Exception as e:
            error_msg = str(e)

            if "429" in error_msg:
                return "⚠️ API quota exceeded. Please wait a minute and try again."

            return f"❌ AI Error: {error_msg}"
       