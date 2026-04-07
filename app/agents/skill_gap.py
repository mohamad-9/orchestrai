from app.schemas.models import SkillGap


# Same job database (keep consistent with job matcher)
JOB_SKILLS = {
    "ai engineer": ["python", "machine learning", "deep learning", "docker", "aws"],
    "backend developer": ["python", "fastapi", "django", "sql", "docker"],
    "data scientist": ["python", "machine learning", "nlp", "sql"],
}


def find_skill_gaps(user_skills: list[str], target_role: str | None = None) -> SkillGap:
    """
    Identify missing skills for a target role.
    """

    if not target_role:
        return SkillGap(missing_skills=[])

    role_key = target_role.lower()

    if role_key not in JOB_SKILLS:
        return SkillGap(missing_skills=[])

    required_skills = set(JOB_SKILLS[role_key])
    user_skills_set = set(user_skills)

    missing = list(required_skills - user_skills_set)

    return SkillGap(missing_skills=missing)