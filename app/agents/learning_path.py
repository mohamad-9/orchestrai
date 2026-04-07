from app.schemas.models import LearningPath


def generate_learning_path(missing_skills: list[str]) -> LearningPath:
    """
    Generate learning recommendations based on missing skills.
    """

    recommendations = []

    for skill in missing_skills:
        recommendations.append(f"Learn {skill}")

    return LearningPath(recommendations=recommendations)