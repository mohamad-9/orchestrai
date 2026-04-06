from app.schemas.models import CVAnalysis


# Simple skill database (we will expand later)
KNOWN_SKILLS = [
    "python",
    "fastapi",
    "django",
    "flask",
    "machine learning",
    "deep learning",
    "nlp",
    "sql",
    "postgresql",
    "mongodb",
    "docker",
    "kubernetes",
    "aws",
    "git",
    "linux",
    "react",
]


def analyze_cv(cv_text: str) -> CVAnalysis:
    """
    Extract skills from CV text.
    """

    cv_text_lower = cv_text.lower()

    detected_skills = []

    for skill in KNOWN_SKILLS:
        if skill in cv_text_lower:
            detected_skills.append(skill)

    return CVAnalysis(skills=detected_skills)