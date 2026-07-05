"""
Study Planner Agent
Responsibility:
- Synthesize a revision notes sheet based on missing topics.
- Generate a calendar schedule to guide preparation over the target days limit.
"""

from src.agents.base import BaseAgent

class StudyPlanner(BaseAgent):
    def generate_plan_and_notes(self, weak_topics: list, days_remaining: int, target_score: float) -> dict:
        """
        Creates a custom study timetable and target study summaries.
        
        Args:
            weak_topics (list): Topics identified as needing reinforcement.
            days_remaining (int): Time remaining until exam.
            target_score (float): Target score of student.
            
        Returns:
            dict: Study plan text/calendar markdown and concise revision notes markdown.
        """
        # Load study_planning.txt prompt template
        # Request formatted output (calendar Markdown & summary Markdown)
        return {}
