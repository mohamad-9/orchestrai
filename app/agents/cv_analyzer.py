from app.services.llm_service import extract_skills_with_llm
from app.schemas.models import CVAnalysis

def normalize_skills(skills: list[str]) -> list[str]:
    mapping = {
        "tensorflow": "deep learning",
        "pytorch": "deep learning",
        "neural networks": "deep learning",
        "transformers": "nlp",
    }

    normalized = []

    for skill in skills:
        skill_lower = skill.lower()
        normalized.append(mapping.get(skill_lower, skill_lower))

    return list(set(normalized))

def analyze_cv(cv_text: str) -> CVAnalysis:
    try:
        skills = extract_skills_with_llm(cv_text)
        skills = normalize_skills(skills)
    except Exception:
        skills = ["python"]  # fallback

    return CVAnalysis(skills=skills)

    

