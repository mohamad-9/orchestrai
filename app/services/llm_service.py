from openai import OpenAI

client = OpenAI()


def extract_skills_with_llm(cv_text: str) -> list[str]:
    """
    Use LLM to extract skills from CV text.
    """

    prompt = f"""
    Extract all technical skills from this CV.
    Return ONLY a Python list.

    CV:
    {cv_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    content = response.choices[0].message.content

    try:
        skills = eval(content)
    except:
        skills = []

    return skills