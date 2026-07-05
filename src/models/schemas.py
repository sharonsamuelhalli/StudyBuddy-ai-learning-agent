from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Topic(BaseModel):
    topic_name: str = Field(description="The core subject topic or chapter name.")
    subtopics: List[str] = Field(default=[], description="Subtopics, key points, or modules inside the topic.")
    priority: str = Field(description="Importance priority relative to exam success. Must be 'High', 'Medium', or 'Low'.")

class SyllabusAnalysis(BaseModel):
    topics: List[Topic] = Field(description="A collection of topics extracted from the syllabus.")

class KnowledgeGap(BaseModel):
    topic_name: str = Field(description="The name of the topic from the syllabus.")
    status: str = Field(description="The level of coverage in the notes: 'Missing' or 'Weak'.")
    description: str = Field(description="Explanation of why this topic is missing or considered weak in the student notes.")

class ReadinessReport(BaseModel):
    readiness_percentage: int = Field(description="Estimated readiness score from 0 to 100 based on notes vs syllabus coverage.")
    gaps: List[KnowledgeGap] = Field(default=[], description="A list of missing or poorly covered syllabus topics.")
    reasoning_summary: str = Field(description="A brief explanation of how the readiness score was determined.")

class QuizQuestion(BaseModel):
    question: str = Field(description="The exam question text.")
    options: Dict[str, str] = Field(description="Four multiple-choice options with keys A, B, C, D.")
    correct_option: str = Field(description="The single correct option key: 'A', 'B', 'C', or 'D'.")
    explanation: str = Field(description="A detailed explanation of why the correct option is right and others are wrong.")

class Quiz(BaseModel):
    questions: List[QuizQuestion] = Field(description="Exactly 10 multiple-choice questions focusing on weak topics.")

class StudyDay(BaseModel):
    day_number: int = Field(description="The sequential day number of study (e.g. 1, 2, 3).")
    topics_to_study: List[str] = Field(description="List of syllabus topics to focus on during this day.")
    study_duration_hours: int = Field(description="Recommended study hours for this day.")
    focus_description: str = Field(description="Detailed hourly schedule or specific instructions on how to revise these topics.")

class StudyPlan(BaseModel):
    schedule: List[StudyDay] = Field(description="Timetable schedule mapped day-by-day.")
    revision_notes_markdown: str = Field(description="A Markdown-formatted study sheet summarizing definitions, formulas, and key points for all weak/missing topics.")

class AgentResult(BaseModel):
    agent_name: str = Field(description="The name of the execution agent.")
    status: str = Field(description="Status of completion: 'Completed', 'Retried', or 'Failed'.")
    execution_time_seconds: float = Field(description="Time elapsed during agent execution.")
    error_message: Optional[str] = Field(None, description="Details of any errors encountered during execution.")

class AgentExecutionResult(BaseModel):
    syllabus: Optional[SyllabusAnalysis] = None
    readiness: Optional[ReadinessReport] = None
    quiz: Optional[Quiz] = None
    study_plan: Optional[StudyPlan] = None
    log: List[AgentResult] = []
