from app.schemas.models import SkillGap

# same database as job matcher
JOB_DATABASE = [
    {
        "title": "AI Engineer",
        "skills": ["python", "machine learning", "deep learning", "docker", "aws"],
    }
]

# 🔥 import normalization from job matcher
from app.agents.job_matcher import normalize_for_matching


def find_skill_gaps(user_skills: list[str], target_role: str | None = None) -> SkillGap:

    user_skills = normalize_for_matching(user_skills)

    for job in JOB_DATABASE:
        if target_role and target_role.lower() not in job["title"].lower():
            continue

        job_skills = job["skills"]

        missing = list(set(job_skills) - set(user_skills))

        return SkillGap(missing_skills=missing)

    return SkillGap(missing_skills=[])