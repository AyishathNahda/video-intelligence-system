from fastapi import FastAPI
from app.services.gemini_service import ask_gemini
app=FastAPI()

@app.get("/")
def home():
    return { "message": "Backend is running"}

@app.get("/test-gemini")
def test_gemini():
    answer=ask_gemini("Explain RAG in simple words")
    return {"response":answer}