from urllib import response

from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_skills_with_llm(cv_text: str) -> list[str]:
    prompt = f"""
You are an expert AI system that extracts technical skills from CVs.

Extract all relevant technical skills from the text below.

Rules:
- Include tools, frameworks, and concepts
- Examples: Python, TensorFlow, NLP, Docker, AWS
- Be comprehensive
- Return ONLY valid JSON

Format:
{{ "skills": ["skill1", "skill2"] }}

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

    print("\n=== LLM RAW RESPONSE ===")
    print(content)
    print("========================\n")

    try:
        import json
        data = json.loads(content)
        return data.get("skills", [])
    except Exception as e:
        print("JSON ERROR:", e)
        return []