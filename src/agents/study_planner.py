"""
Study Planner Agent
Responsibility:
- Synthesize a revision notes sheet based on missing topics.
- Generate a calendar schedule to guide preparation over the target days limit.
"""

"""
Study Planner Agent

Responsibility:
- Combine syllabus + roadmap into a structured plan
"""

from src.agents.base import BaseAgent

class StudyPlanner(BaseAgent):

    def generate_plan_and_notes(self, weak_topics, days_remaining, target_score):

        prompt = self.load_prompt("src/prompts/study_planner.txt")

        roadmap_json = f"""
        Weak Topics: {weak_topics}
        Days Remaining: {days_remaining}
        Target Score: {target_score}
        """

        prompt = prompt.replace("{roadmap_json}", roadmap_json)

        response = self.generate_response(prompt)

        return response

    