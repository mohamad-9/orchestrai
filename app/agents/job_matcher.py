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


def match_jobs(user_skills: list[str], target_role: str | None = None) -> list[JobMatch]:
    """
    Match user skills with jobs.
    """

    results = []

    for job in JOB_DATABASE:
        job_skills = job["skills"]

        # Calculate overlap
        matched = set(user_skills) & set(job_skills)
        score = len(matched) / len(job_skills)

        # Optional filtering by target role
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