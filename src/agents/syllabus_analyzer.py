"""
Syllabus Analyzer Agent
Responsibility:
- Extract main topics, subtopics, and hierarchy structure from the syllabus text.
- Standardize output into structured format.
"""

from src.agents.base import BaseAgent

class SyllabusAnalyzer(BaseAgent):
    def analyze_syllabus(self, syllabus_text: str) -> dict:
        """
        Parses syllabus text and extracts a structured JSON list of key topics.
        
        Args:
            syllabus_text (str): Extracted raw syllabus text.
            
        Returns:
            dict: Structured topics and priorities list.
        """
        # Load syllabus_analysis.txt prompt template
        # Call Gemini client with JSON response schema if desired
        return {}
