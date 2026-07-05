# StudyBuddy AI Learning Agent MVP

StudyBuddy is an AI-powered agent designed to help students prepare for exams by analyzing their syllabus and study notes. 

## Folder Structure

```text
app/
├── .env.example                  # Template for local environment variables
├── .gitignore                    # Git ignore file (vetting venv, .env, __pycache__)
├── README.md                     # This documentation file
├── requirements.txt              # Project dependencies
├── app.py                        # Streamlit Main Entrypoint (UI and routing)
│
└── src/                          # Application source code directory
    ├── __init__.py
    ├── config.py                 # Application configuration & API keys validation
    ├── pdf_extractor.py          # PDF text extraction utilities (using pdfplumber)
    │
    ├── agents/                   # LLM Agent orchestration layer
    │   ├── __init__.py
    │   ├── base.py               # Shared Agent client initialization and helper methods
    │   ├── syllabus_analyzer.py  # Syllabus Agent (analyzes topics, structures roadmap)
    │   ├── notes_analyzer.py     # Notes Agent (compares notes vs syllabus, finds gaps)
    │   ├── quiz_generator.py     # Quiz Agent (generates MCQs targeting weak areas)
    │   └── study_planner.py      # Planner Agent (generates study schedule & revision notes)
    │
    └── prompts/                  # System & User prompts template store
        ├── syllabus_analysis.txt
        ├── notes_comparison.txt
        ├── quiz_generation.txt
        └── study_planning.txt
```

## Running the App (Once logic is implemented)

1. **Set up virtual environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure API Key**:
   Copy `.env.example` to `.env` and fill in your Google Gemini API key:
   ```bash
   cp .env.example .env
   ```
4. **Run Streamlit**:
   ```bash
   streamlit run app.py
   ```
