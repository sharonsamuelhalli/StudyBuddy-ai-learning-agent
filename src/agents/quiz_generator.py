"""
Quiz Generator Agent
Responsibility:
- Formulate 10 Multiple Choice Questions (MCQs) focusing heavily on the identified weak/missing syllabus areas.
- Provide answer keys, choices, and detailed explanations for correctness.
"""

from src.agents.base import BaseAgent

class QuizGenerator(BaseAgent):
    def generate_targeted_quiz(self, weak_topics: list) -> list:
        """
        Generates 10 targeted MCQs based on specific weak topics.
        
        Args:
            weak_topics (list): Topics identified as missing or weak.
            
        Returns:
            list: List of quiz questions (JSON format, containing question text, options, correct choice, explanation).
        """
        # Load quiz_generation.txt prompt template
        # Request structured JSON format conforming to MCQ schema
        return []
