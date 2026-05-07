RELATED_SKILLS = {

    "deep learning": [
        "tensorflow",
        "pytorch",
        "neural networks"
    ],

    "backend development": [
        "fastapi",
        "apis",
        "rest api"
    ],

    "containerization": [
        "docker",
        "kubernetes"
    ],

    "cloud computing": [
        "aws",
        "gcp"
    ],

    "frontend development": [
        "react",
        "javascript"
    ]
}


def get_related_skills(skill: str) -> list[str]:

    return RELATED_SKILLS.get(
        skill.lower(),
        []
    )