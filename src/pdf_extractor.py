"""
PDF Extraction Utility for StudyBuddy AI Learning Agent.

Responsibilities:
- Extract text from uploaded PDF files.
- Handle multi-page PDFs.
- Return a single string containing all extracted text.
"""

import pdfplumber


def extract_text_from_pdf(pdf_file) -> str:
    """
    Extract text from a PDF file.

    Args:
        pdf_file: Uploaded PDF file (Streamlit UploadedFile or file path)

    Returns:
        str: Combined text from all pages.
    """

    extracted_text = ""

    try:
        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:
                text = page.extract_text()

                if text:
                    extracted_text += text + "\n"

        return extracted_text.strip()

    except Exception as e:
        raise Exception(f"Error extracting PDF text: {e}")