from app.services.llm_service import extract_skills_with_llm
from app.schemas.models import CVAnalysis


def analyze_cv(cv_text: str) -> CVAnalysis:
    """
    Extract skills using LLM.
    """

    skills = extract_skills_with_llm(cv_text)

    return CVAnalysis(skills=skills)