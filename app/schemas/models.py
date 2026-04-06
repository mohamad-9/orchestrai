from pydantic import BaseModel
from typing import List, Optional


# -------- INPUT --------
class CVRequest(BaseModel):
    cv_text: str
    target_role: Optional[str] = None


# -------- AGENT OUTPUTS --------
class CVAnalysis(BaseModel):
    skills: List[str]


class JobMatch(BaseModel):
    job_title: str
    match_score: float


class SkillGap(BaseModel):
    missing_skills: List[str]


class LearningPath(BaseModel):
    recommendations: List[str]


# -------- FINAL RESPONSE --------
class FinalResponse(BaseModel):
    skills: List[str]
    matched_jobs: List[JobMatch]
    skill_gaps: List[str]
    learning_path: List[str]