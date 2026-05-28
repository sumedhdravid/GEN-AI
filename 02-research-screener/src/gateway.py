from pydantic import BaseModel, Field
from typing import List

class AuditEvaluationSchema(BaseModel):
    """Enforces rigid structured JSON boundaries around LLM validation payloads."""
    candidate_relevancy_percentage: float = Field(description="Deterministic match ranking score from 0.0 to 100.0.")
    matched_breakthroughs: List[str] = Field(description="Key structural technological solutions discovered inside the content.")
    missing_technical_competencies: List[str] = Field(description="Gaps found when comparing core document text against evaluation criteria.")
    justification_summary: str = Field(description="Strictly object-oriented data analysis validating the given metrics.")
