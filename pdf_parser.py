from pypdf import PdfReader
from typing import Optional

def extract_text_from_pdf(file_path: str) -> Optional[str]:
    """
    Extracts text content from PDF files
    Args:
        file_path: Path to the PDF file
    Returns:
        Extracted text as string, or None if failed
    """
    try:
        text = ""
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""  # Handle None returns
        return text.strip() if text else None
    except Exception as e:
        print(f"PDF extraction error: {str(e)}")
        return None