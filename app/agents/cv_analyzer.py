from app.services.llm_service import extract_skills_with_llm
from app.schemas.models import CVAnalysis, AgentMessage


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


def analyze_cv(cv_text: str) -> AgentMessage:
    skills = extract_skills_with_llm(cv_text)
    skills = normalize_skills(skills)

    return AgentMessage(
        sender="cv_analyzer",
        receiver="coordinator",
        content={"skills": skills}
    )
    

