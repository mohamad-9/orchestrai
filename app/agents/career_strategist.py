from openai import OpenAI
import os

from app.services.readiness_scorer import (
    calculate_readiness_score
)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_career_strategy(
    skills,
    skill_gaps,
    target_role,
    match_score
):

    matched_skills_count = max(
        1,
        int(match_score * 5)
    )

    total_required_skills = 5

    readiness_score = calculate_readiness_score(
        skills=skills,
        matched_skills_count=matched_skills_count,
        total_required_skills=total_required_skills
    )

    # smarter level classification
    if readiness_score >= 80:
        level = "Advanced"

    elif readiness_score >= 60:
        level = "Intermediate"

    else:
        level = "Beginner"

    prompt = f"""
    You are an expert AI career strategist.

    User target role:
    {target_role}

    Current skills:
    {skills}

    Missing skills:
    {skill_gaps}

    Career readiness:
    {readiness_score}/100

    Career level:
    {level}

    Generate:
    1. Strategic evaluation
    2. Biggest strength
    3. Biggest weakness
    4. Recommended next focus
    5. One motivational sentence

    Keep the response concise,
    strategic,
    intelligent,
    and professional.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "readiness_score": readiness_score,
        "level": level,
        "strategy": response.choices[0].message.content
    }