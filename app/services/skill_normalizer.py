NORMALIZATION_MAP = {

    # AI / ML
    "tensorflow": "deep learning",
    "pytorch": "deep learning",
    "neural networks": "deep learning",
    "transformers": "nlp",
    "llms": "large language models",
    "machine learning": "machine learning",

    # Backend
    "fastapi": "backend development",
    "apis": "backend development",
    "rest api": "backend development",

    # DevOps
    "docker": "containerization",
    "kubernetes": "containerization",

    # Cloud
    "aws": "cloud computing",
    "gcp": "cloud computing",

    # Frontend
    "react": "frontend development",
    "javascript": "frontend development",
}


def normalize_skills(skills: list[str]) -> list[str]:

    normalized = []

    for skill in skills:

        skill_lower = skill.lower().strip()

        canonical_skill = NORMALIZATION_MAP.get(
            skill_lower,
            skill_lower
        )

        normalized.append(canonical_skill)

    return list(set(normalized))