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

# 🔥 Improved skill equivalence (VERY IMPORTANT)
SKILL_EQUIVALENTS = {
    "tensorflow": "deep learning",
    "pytorch": "deep learning",
    "neural networks": "deep learning",

    "transformers": "nlp",
    "nlp": "machine learning",
    "llms": "machine learning",
    "large language models (llms)": "machine learning",

    "hugging face inference api": "machine learning",
}


def normalize_for_matching(skills: list[str]) -> list[str]:
    normalized = []

    for skill in skills:
        skill_lower = skill.lower()

        # keep original
        normalized.append(skill_lower)

        # add mapped version
        if skill_lower in SKILL_EQUIVALENTS:
            normalized.append(SKILL_EQUIVALENTS[skill_lower])

    return list(set(normalized))


def match_jobs(user_skills: list[str], target_role: str | None = None) -> list[JobMatch]:
    results = []

    # 🔥 normalize skills
    user_skills = normalize_for_matching(user_skills)

    for job in JOB_DATABASE:
        job_skills = job["skills"]

        matched = set(user_skills) & set(job_skills)
        missing = set(job_skills) - set(user_skills)

        # 🔥 NEW REALISTIC SCORING
        coverage = len(matched) / len(job_skills)

        bonus = min(len(user_skills) / 20, 0.3)  # cap bonus

        score = coverage + bonus
        score = min(score, 0.95)  # NEVER 1 unless perfect

        # filter by role
        if target_role:
            if target_role.lower() not in job["title"].lower():
                continue

        # 🔥 IMPROVED REASONING
        reason = (
            f"You match {len(matched)} required skills: {', '.join(sorted(matched)) if matched else 'none'}. "
            f"You also have related skills: {', '.join(sorted(user_skills))}. "
            f"Missing key skills: {', '.join(sorted(missing)) if missing else 'none'}."
        )

        results.append(
            JobMatch(
                job_title=job["title"],
                match_score=round(score, 2),
                reasoning=reason,
            )
        )

    return results