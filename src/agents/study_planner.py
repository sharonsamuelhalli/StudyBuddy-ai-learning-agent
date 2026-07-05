from src.agents.base import BaseAgent

class StudyPlanner(BaseAgent):

    def generate_plan_and_notes(self, weak_topics, days_remaining, target_score):

        # read prompt file
        with open("src/prompts/study_planning.txt", "r") as f:
            prompt_template = f.read()

        # create prompt
        prompt = prompt_template.format(
            weak_topics=", ".join(weak_topics),
            days_remaining=days_remaining,
            target_score=target_score
        )

        # call Gemini
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return {
            "study_plan": response.text,
            "revision_notes": response.text
        }