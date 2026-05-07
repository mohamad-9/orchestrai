from app.services.llm_service import extract_skills_with_llm
from app.schemas.models import CVAnalysis, AgentMessage
from app.services.skill_normalizer import normalize_skills




def analyze_cv(cv_text: str) -> AgentMessage:

    skills = extract_skills_with_llm(cv_text)

    skills = normalize_skills(skills)

    return AgentMessage(
        sender="cv_analyzer",
        receiver="coordinator",
        content={"skills": skills}
    )

def analyze_cv(cv_text: str) -> AgentMessage:
    skills = extract_skills_with_llm(cv_text)
    skills = normalize_skills(skills)

    return AgentMessage(
        sender="cv_analyzer",
        receiver="coordinator",
        content={"skills": skills}
    )
    

