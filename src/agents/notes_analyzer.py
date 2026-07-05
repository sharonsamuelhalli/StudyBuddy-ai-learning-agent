"""
Notes Analyzer Agent
Responsibility:
- Compare the student's study notes text against the structured syllabus topics.
- Identify weak topics or absolute gaps (uncovered syllabus areas).
- Compute an overall readiness score estimate.
"""

from src.agents.base import BaseAgent

class NotesAnalyzer(BaseAgent):
    def compare_notes_to_syllabus(self, structured_syllabus: dict, notes_text: str) -> dict:
        """
        Compares notes against syllabus topics.
        
        Args:
            structured_syllabus (dict): Output from SyllabusAnalyzer
            notes_text (str): Raw text extracted from notes PDF
            
        Returns:
            dict: Gap analysis results containing weak topics, missing topics, and estimated readiness percentage.
        """
        # Load notes_comparison.txt prompt template
        # Request a structured JSON comparison from Gemini API
        return {}
