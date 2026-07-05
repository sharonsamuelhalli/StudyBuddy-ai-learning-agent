"""
Syllabus Analyzer Agent

Responsibility:
- Analyze syllabus text.
- Extract important topics.
- Return structured JSON.
"""

from src.agents.base import BaseAgent


class SyllabusAnalyzer(BaseAgent):

    def analyze_syllabus(self, syllabus_text: str) -> str:
        """
        Analyze syllabus using Gemini.

        Args:
            syllabus_text (str): Extracted syllabus text.

        Returns:
            str: Gemini JSON response.
        """

        prompt = self.load_prompt("src/prompts/syllabus_analysis.txt")

        prompt = prompt.replace(
            "{syllabus_text}",
            syllabus_text
        )

        response = self.generate_response(prompt)

        return response