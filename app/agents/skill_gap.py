from app.schemas.models import SkillGap

from app.services.semantic_skills import get_related_skills


# same database as job matcher
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
    }
]


def is_skill_covered(
    user_skills: list[str],
    required_skill: str
):

    # direct match
    if required_skill in user_skills:
        return True

    # semantic match
    for user_skill in user_skills:

        related = get_related_skills(user_skill)

        if required_skill in related:
            return True

    return False


def find_skill_gaps(
    user_skills: list[str],
    target_role: str | None = None
) -> SkillGap:

    user_skills = [
        s.lower()
        for s in user_skills
    ]

    for job in JOB_DATABASE:

        if target_role:

            if target_role.lower() not in job["title"].lower():
                continue

        required_skills = [
            s.lower()
            for s in job["skills"]
        ]

        missing = []

        for required_skill in required_skills:

            covered = is_skill_covered(
                user_skills,
                required_skill
            )

            if not covered:
                missing.append(required_skill)

        return SkillGap(
            missing_skills=missing
        )

    return SkillGap(
        missing_skills=[]
    )