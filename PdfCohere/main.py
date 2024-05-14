# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pdf_processor import process_pdf
from query_handler import generate_response

app = FastAPI()

# Almacenamiento en memoria para los embeddings
embeddings_storage = {}

contexts_storage = {}


@app.get("/process-pdf/")
def process_pdf_endpoint(pdf_url: str):
    try:
        print("Antes de process_pdf:", embeddings_storage)
        pdf_id = process_pdf(pdf_url, embeddings_storage, contexts_storage) 
        return {"message": "PDF procesado exitosamente", "pdf_id": pdf_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/ask-question/")
def ask_question_endpoint(pdf_id: str, query: str):
    try:
        print("Después de process_pdf:", embeddings_storage)
        answer, relevant_contexts = generate_response(query, pdf_id, embeddings_storage, contexts_storage)
        return {"query": query, "answer": answer, "Most Relevants Contexts": relevant_contexts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

