from sqlalchemy.orm import Session
from app.models import AnalysisResult

def save_analysis(db: Session, original_text: str, summary: str, metadata: dict, keywords: list):
    db_obj = AnalysisResult(
        original_text=original_text,
        summary=summary,
        metadata_json=metadata,
        keywords=keywords
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return {
        "id": db_obj.id,
        "summary": db_obj.summary,
        "metadata": db_obj.metadata_json,
        "keywords": db_obj.keywords
    }
