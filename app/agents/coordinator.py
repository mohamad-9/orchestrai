from app.agents.cv_analyzer import analyze_cv
from app.agents.job_matcher import match_jobs
from app.agents.skill_gap import find_skill_gaps
from app.agents.learning_path import generate_learning_path

from app.schemas.models import FinalResponse


def run_pipeline(cv_text: str, target_role: str | None = None) -> FinalResponse:
    """
    Main orchestration pipeline.
    """

    # 1️⃣ CV Analysis
    cv_analysis = analyze_cv(cv_text)

    # 2️⃣ Job Matching
    job_matches = match_jobs(cv_analysis.skills, target_role)

    # 3️⃣ Skill Gap Analysis
    skill_gaps = find_skill_gaps(cv_analysis.skills, target_role)

    # 4️⃣ Learning Path
    learning_path = generate_learning_path(skill_gaps.missing_skills)

    # 5️⃣ Combine results
    return FinalResponse(
        skills=cv_analysis.skills,
        matched_jobs=job_matches,
        skill_gaps=skill_gaps.missing_skills,
        learning_path=learning_path.recommendations
    )