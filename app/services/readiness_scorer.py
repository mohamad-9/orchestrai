ENGINEERING_SKILLS = [
    "backend development",
    "frontend development",
    "containerization",
    "cloud deployment",
    "sql",
    "postgresql",
    "mysql",
    "git",
]

AI_SKILLS = [
    "machine learning",
    "deep learning",
    "nlp",
    "large language models",
    "hugging face inference api",
]



def calculate_readiness_score(
    skills,
    matched_skills_count,
    total_required_skills
):

    # core matching score
    coverage_score = (
        matched_skills_count / total_required_skills
    ) * 60

    # engineering maturity
    engineering_bonus = 0

    for skill in skills:

        if skill.lower() in ENGINEERING_SKILLS:
            engineering_bonus += 3

    engineering_bonus = min(
        engineering_bonus,
        20
    )

    # AI ecosystem familiarity
    ai_bonus = 0

    for skill in skills:

        if skill.lower() in AI_SKILLS:
            ai_bonus += 4

    ai_bonus = min(
        ai_bonus,
        20
    )

    final_score = (
        coverage_score
        + engineering_bonus
        + ai_bonus
    )

    final_score = min(
        int(final_score),
        95
    )

    return final_score