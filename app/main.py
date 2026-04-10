from fastapi import FastAPI
from app.schemas.models import CVRequest
from app.agents.coordinator import run_pipeline
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File
from app.services.cv_parser import parse_pdf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.post("/analyze-pdf")
async def analyze_pdf(file: UploadFile = File(...), target_role: str = "AI Engineer"):

    cv_text = parse_pdf(file.file)

    result = run_pipeline(cv_text, target_role, user_id="pdf_user")

    return result


