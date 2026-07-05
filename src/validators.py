"""
Validation Utility Module
Responsibility:
- Validate input variables (days, target score).
- Validate PDF files (size, empty pages).
- Validate and parse JSON responses from Gemini against Pydantic models.
- Provide simple repair/recovery functions for minor JSON syntax issues.
"""

import json
from typing import Type, TypeVar, Tuple, Optional
from pydantic import BaseModel, ValidationError

T = TypeVar('T', bound=BaseModel)

def validate_user_inputs(days_until_exam: int, target_score: float) -> Tuple[bool, str]:
    """Validates user's manual configuration values."""
    if days_until_exam <= 0:
        return False, "Days until exam must be at least 1 day."
    if not (0 <= target_score <= 100):
        return False, "Target score must be between 0% and 100%."
    return True, "Success"

def validate_pdf_file(pdf_file) -> Tuple[bool, str]:
    """Basic validation for uploaded PDF file objects."""
    if pdf_file is None:
        return False, "No file uploaded."
    
    # Check file size (e.g., limit to 10MB to avoid long timeouts in MVP)
    max_size_bytes = 10 * 1024 * 1024
    pdf_file.seek(0, 2)  # Seek to end
    file_size = pdf_file.tell()
    pdf_file.seek(0)  # Reset
    
    if file_size > max_size_bytes:
        return False, f"File size exceeds limit of 10MB (Current: {file_size / (1024 * 1024):.2f}MB)."
        
    if not pdf_file.name.lower().endswith('.pdf'):
        return False, "File must be a PDF."
        
    return True, "Success"

def validate_and_parse_json(raw_text: str, schema_class: Type[T]) -> Tuple[Optional[T], Optional[str]]:
    """
    Validates and parses a string response from Gemini against a Pydantic model.
    Attempts basic cleanup if the string contains markdown blocks or minor issues.
    
    Args:
        raw_text (str): The raw model output.
        schema_class (Type[T]): The expected Pydantic model class.
        
    Returns:
        Tuple[Optional[T], Optional[str]]: (Parsed object, error message if any)
    """
    clean_text = raw_text.strip()
    
    # Strip markdown wrapper if present
    if clean_text.startswith("```json"):
        clean_text = clean_text[7:]
    elif clean_text.startswith("```"):
        clean_text = clean_text[3:]
        
    if clean_text.endswith("```"):
        clean_text = clean_text[:-3]
        
    clean_text = clean_text.strip()
    
    try:
        data = json.loads(clean_text)
        parsed_object = schema_class.model_validate(data)
        return parsed_object, None
    except json.JSONDecodeError as je:
        return None, f"JSON Decode Error: {je.msg} at position {je.pos}"
    except ValidationError as ve:
        return None, f"Pydantic Validation Error: {str(ve)}"
