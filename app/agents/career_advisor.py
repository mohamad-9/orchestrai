from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_career_advice(skills, skill_gaps, target_role):

    prompt = f"""
    You are an expert AI career advisor.

    A user wants to become a {target_role}.

    Current skills:
    {skills}

    Missing skills:
    {skill_gaps}

    Give:
    1. Short evaluation of the user profile
    2. Main strengths
    3. Main weaknesses
    4. Clear next-step advice

    Keep response concise and professional.
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

    return response.choices[0].message.content