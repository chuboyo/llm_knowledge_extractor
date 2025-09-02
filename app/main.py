from fastapi import FastAPI, HTTPException
from app.database import SessionLocal, engine
from app.models import Base
from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.crud import save_analysis
from app.nlp import extract_keywords
from app.llm import analyze_text


Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(data: AnalyzeRequest):
    try:
        keywords = extract_keywords(data.text)
        summary, metadata = analyze_text(data.text)
        db = SessionLocal()
        result = save_analysis(db, data.text, summary, metadata, keywords)
        db.close()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))