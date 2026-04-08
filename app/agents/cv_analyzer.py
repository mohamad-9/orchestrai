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

        # keep original
        normalized.append(skill_lower)

        # add mapped version if exists
        if skill_lower in mapping:
            normalized.append(mapping[skill_lower])

    return list(set(normalized))

def analyze_cv(cv_text: str) -> CVAnalysis:
    print("🔥 ANALYZE_CV STARTED")

    try:
        skills = extract_skills_with_llm(cv_text)
        skills = normalize_skills(skills)
    except Exception as e:
        print("❌ ERROR IN LLM:", e)
        raise e  # IMPORTANT: do NOT hide it

    return CVAnalysis(skills=skills)
    

