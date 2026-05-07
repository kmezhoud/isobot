from fastapi import APIRouter, UploadFile, File
import shutil
import os

from isobot.utils.word_parser import extract_text
from isobot.services.iso_checker import check_structure
from isobot.services.ai_service import improve_text
from isobot.services.rag.qa import ask
from isobot.utils.pdf_reader import extract_pdf_text
from isobot.services.rag.ingest import ingest_pdf, extract_iso_name

router = APIRouter()



UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

LAST_ISO = None  # temporaire (prototype)

@router.post("/analyze")
async def analyze_document(file: UploadFile):

    global LAST_ISO

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    ext = os.path.splitext(file.filename)[1].lower()

    if ext == ".docx":
        text = extract_word(file_path)
    elif ext == ".pdf":
        iso_name = extract_iso_name(file_path)
        LAST_ISO = iso_name  # 🔥 mémorisation
        
        text = extract_pdf_text(file_path)
        ingest_pdf(file_path, iso_name)
    else:
        return {"error": "Format non supporté"}

    #return {"message": text[:1000]}
    return {"message": f"{iso_name} indexé"}
  
@router.post("/ask")
async def ask_question(question: str, iso_name: str):
    return {"answer": ask(question, iso_name)}
