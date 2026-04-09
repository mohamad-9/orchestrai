from app.agents.cv_analyzer import analyze_cv
from app.agents.job_matcher import match_jobs
from app.agents.skill_gap import find_skill_gaps
from app.agents.learning_path import generate_learning_path
from app.services.memory_service import save_user_data, get_user_data

from app.schemas.models import FinalResponse





def run_pipeline(cv_text: str, target_role: str | None = None, user_id: str = "default_user"):

    # 🔥 LOAD MEMORY
    previous_data = get_user_data(user_id)
    print("🧠 Previous memory:", previous_data)

    # 1️⃣ CV Analyzer
    cv_msg = analyze_cv(cv_text)
    print(f"{cv_msg.sender} → {cv_msg.receiver}: {cv_msg.content}")

    new_skills = cv_msg.content["skills"]

    # 🔥 merge with previous memory
    previous_skills = previous_data.get("skills", [])

    skills = list(set(previous_skills + new_skills))

    # 2️⃣ Job Matcher
    job_matches = match_jobs(skills, target_role)

    # 3️⃣ Skill Gap
    skill_gaps = find_skill_gaps(skills, target_role)

    # 4️⃣ Learning Path
    learning_path = generate_learning_path(skill_gaps.missing_skills)

    # 🔥 SAVE MEMORY
    save_user_data(user_id, {
        "skills": skills,
        "target_role": target_role
    })

    return FinalResponse(
        skills=skills,
        matched_jobs=job_matches,
        skill_gaps=skill_gaps.missing_skills,
        learning_path=learning_path.recommendations
    )