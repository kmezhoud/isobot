from fastapi import APIRouter, UploadFile, File
import shutil
import os

from isobot.utils.word_parser import extract_text
from isobot.services.iso_checker import check_structure
from isobot.services.ai_service import improve_text
from isobot.services.rag.qa import ask
from isobot.utils.pdf_reader import extract_pdf_text
from isobot.services.rag.ingest import ingest_pdf

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/analyze")
async def analyze_document(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ext = os.path.splitext(file.filename)[1].lower()

    if ext == ".docx":
        text = extract_word(file_path)
    elif ext == ".pdf":
        text = extract_pdf_text(file_path)
        ingest_pdf(file_path)
    else:
        return {"error": "Format non supporté"}

    return {"text_preview": text[:1000]}
  
  
@router.post("/ask")
async def ask_question(question: str):
    return {"answer": ask(question)}
