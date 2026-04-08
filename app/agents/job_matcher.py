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

# Skill equivalence mapping
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

        # keep original
        normalized.append(skill_lower)

        # add equivalent skill
        if skill_lower in SKILL_EQUIVALENTS:
            normalized.append(SKILL_EQUIVALENTS[skill_lower])

    return list(set(normalized))


def match_jobs(user_skills: list[str], target_role: str | None = None) -> list[JobMatch]:
    results = []

    # 🔥 normalize user skills
    user_skills = normalize_for_matching(user_skills)

    for job in JOB_DATABASE:
        job_skills = job["skills"]

        # match + missing
        matched = set(user_skills) & set(job_skills)
        missing = set(job_skills) - set(user_skills)

        # 🔥 improved scoring
        score = (len(matched) + 0.5 * len(user_skills)) / len(job_skills)
        score = min(score, 1.0)

        # optional filter
        if target_role:
            if target_role.lower() not in job["title"].lower():
                continue

        # 🔥 reasoning (clean + readable)
        reason = (
            f"Matched skills: {', '.join(sorted(matched)) if matched else 'none'}. "
            f"Missing skills: {', '.join(sorted(missing)) if missing else 'none'}."
        )

        results.append(
            JobMatch(
                job_title=job["title"],
                match_score=round(score, 2),
                reasoning=reason,
            )
        )

    return results