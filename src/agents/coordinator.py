"""
Coordinator Agent
Responsibility:
- Receives uploaded files and configuration parameters.
- Triggers the execution pipeline of the specialized agents sequentially or concurrently.
- Validates the intermediate and final JSON outputs against the Pydantic schemas.
- Log execution steps (status, timestamps, success/failure) to drive the UI timeline.
- Gracefully handles individual agent failures using default fallbacks or retries.
- Consolidates all results into an AgentExecutionResult.
"""

import time
from typing import Callable, Any
from src.agents.base import BaseAgent
from src.agents.syllabus_analyzer import SyllabusAnalyzer
from src.agents.notes_analyzer import NotesAnalyzer
from src.agents.quiz_generator import QuizGenerator
from src.agents.study_planner import StudyPlanner
from src.models.schemas import AgentExecutionResult, AgentResult, SyllabusAnalysis, ReadinessReport, Quiz, StudyPlan
from src.validators import validate_and_parse_json

class CoordinatorAgent(BaseAgent):
    def __init__(self, api_key: str = None):
        super().__init__(api_key=api_key)
        self.syllabus_analyzer = SyllabusAnalyzer(api_key=self.api_key)
        self.notes_analyzer = NotesAnalyzer(api_key=self.api_key)
        self.quiz_generator = QuizGenerator(api_key=self.api_key)
        self.study_planner = StudyPlanner(api_key=self.api_key)

    def run_pipeline(
        self, 
        syllabus_text: str, 
        notes_text: str, 
        days_remaining: int, 
        target_score: float,
        timeline_callback: Callable[[str, str], None] = None
    ) -> AgentExecutionResult:
        """
        Executes the entire agent coordination pipeline step-by-step.
        
        Args:
            syllabus_text (str): Raw text of the syllabus.
            notes_text (str): Raw text of the study notes.
            days_remaining (int): Time constraint.
            target_score (float): Target readiness percentage.
            timeline_callback (Callable): Callback function (agent_name, status) to push timeline updates to the UI.
            
        Returns:
            AgentExecutionResult: Cohesive structured execution result block.
        """
        result = AgentExecutionResult()
        
        def log_status(agent_name: str, status: str, elapsed: float = 0.0, error: str = None):
            result.log.append(AgentResult(
                agent_name=agent_name,
                status=status,
                execution_time_seconds=elapsed,
                error_message=error
            ))
            if timeline_callback:
                timeline_callback(agent_name, status)

        # ----------------------------------------------------
        # Step 1: Syllabus Analyzer
        # ----------------------------------------------------
        t0 = time.time()
        log_status("Syllabus Agent", "Running")
        try:
            # Under actual implementation, this will send the prompt with syllabus_text to Gemini API
            # For skeleton, we return empty structured objects or call the sub-agent
            syllabus_data = self.syllabus_analyzer.analyze_syllabus(syllabus_text)
            # validation logic
            # parsed_syllabus, err = validate_and_parse_json(raw_json_str, SyllabusAnalysis)
            elapsed = time.time() - t0
            log_status("Syllabus Agent", "Completed", elapsed)
        except Exception as e:
            elapsed = time.time() - t0
            log_status("Syllabus Agent", "Failed", elapsed, str(e))
            # Handle fail / fallback
            
        # ----------------------------------------------------
        # Step 2: Notes Analyzer & Gap Detector
        # ----------------------------------------------------
        t0 = time.time()
        log_status("Notes Agent", "Running")
        try:
            # Compare notes against syllabus
            readiness_data = self.notes_analyzer.compare_notes_to_syllabus({}, notes_text)
            elapsed = time.time() - t0
            log_status("Notes Agent", "Completed", elapsed)
        except Exception as e:
            elapsed = time.time() - t0
            log_status("Notes Agent", "Failed", elapsed, str(e))
            
        # ----------------------------------------------------
        # Step 3: Quiz Generator
        # ----------------------------------------------------
        t0 = time.time()
        log_status("Quiz Agent", "Running")
        try:
            quiz_data = self.quiz_generator.generate_targeted_quiz([])
            elapsed = time.time() - t0
            log_status("Quiz Agent", "Completed", elapsed)
        except Exception as e:
            elapsed = time.time() - t0
            log_status("Quiz Agent", "Failed", elapsed, str(e))

        # ----------------------------------------------------
        # Step 4: Study Planner Agent
        # ----------------------------------------------------
        t0 = time.time()
        log_status("Study Planner Agent", "Running")
        try:
            plan_data = self.study_planner.generate_plan_and_notes([], days_remaining, target_score)
            elapsed = time.time() - t0
            log_status("Study Planner Agent", "Completed", elapsed)
        except Exception as e:
            elapsed = time.time() - t0
            log_status("Study Planner Agent", "Failed", elapsed, str(e))
            
        return result
