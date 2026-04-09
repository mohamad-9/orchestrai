from fastapi import FastAPI
from app.schemas.models import CVRequest
from app.agents.coordinator import run_pipeline

app = FastAPI()


@app.get("/")
def root():
    return {"message": "OrchestrAI is running 🚀"}




@app.post("/analyze")
def analyze_cv(request: CVRequest):
    result = run_pipeline(
        request.cv_text,
        request.target_role,
        request.user_id   # 🔥 NEW
    )
    return result