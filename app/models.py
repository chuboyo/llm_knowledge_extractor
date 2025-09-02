from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(String)
    summary = Column(String)
    metadata_json = Column(JSON)
    keywords = Column(JSON)
