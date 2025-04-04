import os
from pdf_parser import extract_text_from_pdf  # Import specific function
from docx_parser import extract_text_from_docx  # Import specific function
from database import Database  # Import Database class

# Initialize database connection
db = Database()

def process_file(filepath):
    filename = os.path.basename(filepath)
    filetype = filename.split('.')[-1].lower()

    if filetype == 'pdf':
        content = extract_text_from_pdf(filepath)  # Now properly imported
    elif filetype == 'docx':
        content = extract_text_from_docx(filepath)  # Now properly imported
    else:
        print(f"Unsupported file type: {filetype}")
        return

    if content:
        doc_id = db.add_document(filename, content, filetype, filepath)
        print(f"Added document ID: {doc_id}")
    else:
        print("Failed to extract content")

# Example usage
if _name_ == "_main_":
    file_to_process = "test.pdf"  # Change to your file path
    if os.path.exists(file_to_process):
        process_file(file_to_process)
    else:
        print(f"File not found: {file_to_process}")