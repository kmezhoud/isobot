from fastapi import APIRouter, UploadFile, File
import shutil
import os

from isobot.utils.word_parser import extract_text
from isobot.services.iso_checker import check_structure
from isobot.services.ai_service import improve_text

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/analyze")
async def analyze_document(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)
    structure = check_structure(text)
    improved = improve_text(text)

    return {
        "structure_check": structure,
        "improved_version": improved
    }
