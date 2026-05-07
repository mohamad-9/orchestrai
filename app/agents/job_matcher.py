from app.schemas.models import JobMatch

from app.services.semantic_skills import get_related_skills


# Mock job database
JOB_DATABASE = [
    {
        "title": "AI Engineer",
        "skills": [
            "python",
            "machine learning",
            "deep learning",
            "docker",
            "aws",
        ],
    },
    {
        "title": "Backend Developer",
        "skills": [
            "python",
            "fastapi",
            "django",
            "sql",
            "docker",
        ],
    },
    {
        "title": "Data Scientist",
        "skills": [
            "python",
            "machine learning",
            "nlp",
            "sql",
        ],
    },
]


def semantic_match_score(
    user_skills: list[str],
    required_skills: list[str]
):

    matched = set()

    semantic_matches = []

    for required_skill in required_skills:

        # direct match
        if required_skill in user_skills:
            matched.add(required_skill)
            continue

        # semantic match
        for user_skill in user_skills:

            related_skills = get_related_skills(user_skill)

            if required_skill in related_skills:

                semantic_matches.append(
                    f"{user_skill} → {required_skill}"
                )

                matched.add(required_skill)

    return matched, semantic_matches


def match_jobs(
    user_skills: list[str],
    target_role: str | None = None
) -> list[JobMatch]:

    results = []

    user_skills = [s.lower() for s in user_skills]

    for job in JOB_DATABASE:

        # filter by role
        if target_role:
            if target_role.lower() not in job["title"].lower():
                continue

        required_skills = [
            s.lower()
            for s in job["skills"]
        ]

        matched, semantic_matches = semantic_match_score(
            user_skills,
            required_skills
        )

        missing = set(required_skills) - matched

        # smarter scoring
        coverage = len(matched) / len(required_skills)

        bonus = min(
            len(user_skills) / 20,
            0.25
        )

        score = coverage + bonus

        score = min(score, 0.95)

        # reasoning
        reasoning = (
            f"You match {len(matched)} required skills: "
            f"{', '.join(sorted(matched)) if matched else 'none'}. "
        )

        if semantic_matches:

            reasoning += (
                f"Semantic matches detected: "
                f"{', '.join(semantic_matches)}. "
            )

        reasoning += (
            f"Missing key skills: "
            f"{', '.join(sorted(missing)) if missing else 'none'}."
        )

        results.append(
            JobMatch(
                job_title=job["title"],
                match_score=round(score, 2),
                reasoning=reasoning,
            )
        )

    return results