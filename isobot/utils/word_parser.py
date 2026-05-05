from docx import Document

def extract_text(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])
