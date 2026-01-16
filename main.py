from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse

from src.rag import process_pdf_and_answer

app = FastAPI(title="RAG Chat with PDF API", version="1.0")


@app.get("/")
def home():
    return {"status": "ok", "message": "RAG Chat with PDF FastAPI is running"}


@app.post("/ask")
async def ask_pdf(
    pdf: UploadFile = File(...),
    question: str = Form(...)
):
    if not pdf.filename.lower().endswith(".pdf"):
        return JSONResponse({"error": "Only PDF files allowed"}, status_code=400)

    pdf_bytes = await pdf.read()
    result = process_pdf_and_answer(pdf_bytes, question)
    return result

