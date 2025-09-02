from pydantic import BaseModel
from typing import List, Dict

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    id: int
    summary: str
    metadata: Dict
    keywords: List[str]
