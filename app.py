"""
StudyBuddy: AI Learning Agent - Modern Dashboard Interface
Responsibility:
- Render input section (Syllabus PDF, Notes PDF, Days until exam, Target score).
- Show real-time multi-agent execution timeline (Coordinator, Syllabus, Notes, Quiz, Planner).
- Display a comprehensive Results Dashboard containing Readiness metrics, Gaps list, Study timetable, Revision summaries, and an Interactive Quiz.
"""

import streamlit as st
import time

def run_agent_simulation():
    """Simulates agent execution pipeline to demonstrate timeline visuals."""
    timeline_placeholder = st.empty()
    
    agents = [
        "Coordinator Agent",
        "Syllabus Analyzer Agent",
        "Notes Analyzer Agent",
        "Quiz Generator Agent",
        "Study Planner Agent"
    ]
    
    statuses = {a: "⏳ Waiting" for a in agents}
    
    for i, agent in enumerate(agents):
        statuses[agent] = "⚡ Running..."
        # Update timeline
        with timeline_placeholder.container():
            st.subheader("🤖 Multi-Agent Execution Timeline")
            for a, status in statuses.items():
                if "Completed" in status:
                    st.write(f"✅ **{a}**: {status}")
                elif "Running" in status:
                    st.write(f"🔵 **{a}**: {status}")
                else:
                    st.write(f"⚪ **{a}**: {status}")
        time.sleep(1)
        statuses[agent] = "✅ Completed"
        
    timeline_placeholder.empty()

def main():
    st.set_page_config(
        page_title="StudyBuddy: AI Learning Agent",
        page_icon="🎓",
        layout="wide"
    )
    
    st.title("🎓 StudyBuddy: AI Learning Agent")
    st.write("A modular multi-agent dashboard that collaborates to prepare you for exams.")
    
    st.markdown("---")
    
    # 2-Column Main Layout: Input Configuration vs Results Dashboard
    col_input, col_result = st.columns([1, 2])
    
    with col_input:
        st.subheader("⚙️ Control Panel")
        st.file_uploader("Upload Syllabus PDF", type=["pdf"], key="syllabus_upload")
        st.file_uploader("Upload Study Notes PDF", type=["pdf"], key="notes_upload")
        
        st.number_input("Days Until Exam", min_value=1, value=7, step=1, key="days_input")
        st.slider("Target Exam Score (%)", min_value=0, max_value=100, value=85, key="score_input")
        
        analyze_btn = st.button("Start AI Analysis", type="primary", use_container_width=True)
        
        if analyze_btn:
            with st.spinner("Initializing Agent Collaboration..."):
                run_agent_simulation()
                st.session_state["analysis_complete"] = True
                st.success("Analysis Finished!")

    with col_result:
        st.subheader("📊 Results Dashboard")
        
        if not st.session_state.get("analysis_complete", False):
            st.info("Configure variables and click **Start AI Analysis** to generate study plans and diagnostics.")
        else:
            # 1. Readiness Metric & Summary
            st.markdown("### 🎯 Exam Readiness Score")
            st.metric(label="Estimated Readiness", value="65%", delta="-20% (Target: 85%)")
            st.info("**Reasoning Summary**: Syllabus contains 12 core topics. Your study notes cover 8 topics in detail, but cover 2 topics weakly and omit 2 topics completely (e.g., *Dynamic Programming* and *Graph Algorithms*).")
            
            # 2. Knowledge Gaps & Weak Areas
            st.markdown("### ⚠️ Identified Knowledge Gaps")
            st.error("- **Dynamic Programming** (Status: *Missing* in Notes)")
            st.warning("- **Graph Algorithms** (Status: *Weak* in Notes)")
            
            # 3. Personalized Study Plan
            st.markdown("### 📅 Personalized Study Plan")
            st.markdown("""
            | Day | Topics to Focus | Study Duration | Recommended Focus |
            | :--- | :--- | :--- | :--- |
            | **Day 1** | Dynamic Programming (Intro, Memoization) | 3 Hours | Read definitions, implement simple Fibonacci |
            | **Day 2** | Dynamic Programming (Tabulation, Knapsack) | 3 Hours | Focus on bottom-up arrays & boundary conditions |
            | **Day 3** | Graph Algorithms (BFS, DFS) | 2.5 Hours | Verify node traversal structures |
            """)
            
            # 4. Revision Notes
            st.markdown("### 📝 Revision Notes (Targeted)")
            st.markdown("""
            #### Topic: Dynamic Programming
            *   **Memoization (Top-Down)**: Storing results of expensive function calls and returning the cached result when the same inputs occur again.
            *   **Tabulation (Bottom-Up)**: Solving subproblems first, storing results in a table (usually an array), and building up to the solution.
            """)
            
            # 5. Practice Quiz
            st.markdown("### 📝 Targeted Practice Quiz (10 MCQs)")
            with st.form("quiz_form"):
                st.markdown("**Question 1**: What is the space complexity of bottom-up Fibonacci tabulation?")
                st.radio("Choose an option:", [
                    "A) O(1) space if optimized",
                    "B) O(N) space using list",
                    "C) O(2^N) space recursive stack",
                    "D) Both A and B are correct"
                ], index=None)
                
                submitted = st.form_submit_handler = st.form_submit_button("Submit Answers")
                if submitted:
                    st.success("Correct Answer: **D**. Explanation: Tabulation typically requires an array of size N resulting in O(N) auxiliary space. However, it can be optimized to O(1) space by only keeping track of the last two calculated values.")

if __name__ == "__main__":
    main()
