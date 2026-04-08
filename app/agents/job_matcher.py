from app.schemas.models import JobMatch


# Mock job database
JOB_DATABASE = [
    {
        "title": "AI Engineer",
        "skills": ["python", "machine learning", "deep learning", "docker", "aws"],
    },
    {
        "title": "Backend Developer",
        "skills": ["python", "fastapi", "django", "sql", "docker"],
    },
    {
        "title": "Data Scientist",
        "skills": ["python", "machine learning", "nlp", "sql"],
    },
]
SKILL_EQUIVALENTS = {
    "tensorflow": "deep learning",
    "pytorch": "deep learning",
    "neural networks": "deep learning",
    "transformers": "nlp",
}

def normalize_for_matching(skills: list[str]) -> list[str]:
    normalized = []

    for skill in skills:
        skill_lower = skill.lower()

        normalized.append(skill_lower)

        if skill_lower in SKILL_EQUIVALENTS:
            normalized.append(SKILL_EQUIVALENTS[skill_lower])

    return list(set(normalized))

def match_jobs(user_skills: list[str], target_role: str | None = None) -> list[JobMatch]:
    results = []

    # 🔥 ADD THIS LINE
    user_skills = normalize_for_matching(user_skills)

    for job in JOB_DATABASE:
        job_skills = job["skills"]

        matched = set(user_skills) & set(job_skills)

        # 🔥 (optional improved scoring)
        score = (len(matched) + 0.5 * len(user_skills)) / len(job_skills)
        score = min(score, 1.0)
        

        if target_role:
            if target_role.lower() not in job["title"].lower():
                continue

        results.append(
            JobMatch(
                job_title=job["title"],
                match_score=round(score, 2),
            )
        )

    return results