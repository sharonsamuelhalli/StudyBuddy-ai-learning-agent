from src.agents.study_planner import StudyPlanner

planner = StudyPlanner()

roadmap_json = {
    "weak_topics": ["Sorting", "Graphs"],
    "days_remaining": 10,
    "target_score": 85
}

result = planner.generate_plan_and_notes(
    weak_topics=roadmap_json["weak_topics"],
    days_remaining=roadmap_json["days_remaining"],
    target_score=roadmap_json["target_score"]
)

print(result)