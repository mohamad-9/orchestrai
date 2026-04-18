# OrchestrAI – Multi-Agent AI Career Assistant 🚀

OrchestrAI is a **hybrid multi-agent AI system** that helps users make smarter career decisions by simulating a team of intelligent agents working together.

The system analyzes CVs, matches job opportunities, identifies skill gaps, and generates personalized learning paths using a combination of **LLM-powered analysis and structured agent logic**.

---

## 💡 Key Features

- 🤖 LLM-based CV analysis (OpenAI)
- 📄 PDF CV upload support
- 🔄 Multi-agent architecture (A2A communication)
- 📊 Explainable job matching (with reasoning)
- 🧠 Memory system (tracks user skills over time)
- 🌐 Full-stack system (FastAPI + React)

---

## 🧠 Architecture

The system consists of specialized agents:

- **Coordinator Agent** – Orchestrates the workflow between agents  
- **CV Analyzer Agent** – Extracts structured skills using AI  
- **Job Matcher Agent** – Performs semantic job matching with scoring  
- **Skill Gap Agent** – Identifies missing skills  
- **Learning Path Agent** – Generates recommendations  

---

## 🔄 System Flow
User → API → Coordinator → Agents → Response


## Detailed flow:
CV → Skill Extraction → Job Matching → Skill Gap → Learning Path



---

## ⚙️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** React (Vite)
- **AI:** OpenAI API (LLM)
- **PDF Parsing:** pdfplumber
- **Database (planned):** PostgreSQL
- **DevOps (next):** Docker

---

## 🎯 Use Case

- Analyze CV (text or PDF)
- Match with relevant job roles
- Identify missing skills
- Generate a learning roadmap

---

## ⚠️ Current Scope

👉 The current implementation is optimized for **technical roles** (AI, Backend, Data).

The architecture is **designed to be extensible** to other domains.

---

## 🚀 Future Improvements

- 🌍 Deployment (Render / Vercel)
- 🐳 Docker support
- 📊 Skill visualization (charts)
- 🔗 Real job data integration
- 🔐 Authentication system

---

## 🔗 Repository

https://github.com/mohamad-9/orchestrai