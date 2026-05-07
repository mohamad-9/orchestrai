import { useState } from "react";

function App() {

  const [cvText, setCvText] = useState("");
  const [targetRole, setTargetRole] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState(null);

  const handleAnalyze = async () => {

    setLoading(true);

    try {

      let response;

      if (file) {

        const formData = new FormData();

        formData.append("file", file);
        formData.append("target_role", targetRole);

        response = await fetch(
          "http://127.0.0.1:8000/analyze-pdf",
          {
            method: "POST",
            body: formData,
          }
        );

      } else {

        response = await fetch(
          "http://127.0.0.1:8000/analyze",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              cv_text: cvText,
              target_role: targetRole,
              user_id: "demo_user",
            }),
          }
        );
      }

      const data = await response.json();

      setResult(data);

    } catch (error) {

      console.error(error);

    }

    setLoading(false);
  };

  return (

    <div style={styles.page}>

      <div style={styles.container}>

        <h1 style={styles.title}>
          OrchestrAI 🚀
        </h1>

        <p style={styles.subtitle}>
          Multi-Agent AI Career Intelligence Platform
        </p>

        {/* HERO */}

        <div style={styles.heroCard}>

          <h2>🧠 AI-Powered Career Strategy</h2>

          <p>
            OrchestrAI uses multiple AI agents to analyze CVs,
            match career opportunities, identify skill gaps,
            and generate intelligent career strategies.
          </p>

        </div>

        {/* INPUT */}

        <div style={styles.card}>

          <h3 style={styles.inputTitle}>
            📄 CV Input
          </h3>

          <label style={styles.label}>
            Paste your CV
          </label>

          <textarea
            placeholder="Paste your CV here..."
            value={cvText}
            onChange={(e) => {

              setCvText(e.target.value);

              if (e.target.value) {
                setFile(null);
              }

            }}
            style={styles.textarea}
            disabled={file !== null}
          />

          <p style={styles.orText}>
            — OR —
          </p>

          <label style={styles.label}>
            Upload CV (PDF)
          </label>

          <input
            type="file"
            accept=".pdf"
            onChange={(e) => {

              setFile(e.target.files[0]);

              if (e.target.files[0]) {
                setCvText("");
              }

            }}
            disabled={cvText.length > 0}
            style={styles.fileInput}
          />

          <label style={styles.label}>
            Target Role
          </label>

          <input
            placeholder="AI Engineer"
            value={targetRole}
            onChange={(e) => setTargetRole(e.target.value)}
            style={styles.input}
          />

          <button
            onClick={handleAnalyze}
            style={styles.button}
          >
            {loading ? "Analyzing..." : "Analyze Career"}
          </button>

        </div>

        {/* RESULTS */}

        {result && (

          <div style={styles.resultsContainer}>

            {/* READINESS */}

            <div style={styles.readinessCard}>

              <h2 style={styles.readinessTitle}>
                🎯 Career Readiness
              </h2>

              <div style={styles.scoreCircle}>
                {result.strategist.readiness_score}%
              </div>

              <h3 style={styles.readinessLevel}>
                {result.strategist.level}
              </h3>

              <div style={styles.progressBar}>

                <div
                  style={{
                    ...styles.progressFill,
                    width: `${result.strategist.readiness_score}%`,
                  }}
                />

              </div>

            </div>

            {/* JOB MATCH */}

            <div style={styles.jobCard}>

              <h2 style={styles.sectionTitle}>
                💼 Job Match
              </h2>

              {result.matched_jobs.map((job, i) => (

                <div key={i}>

                  <h3 style={styles.jobTitle}>
                    {job.job_title}
                  </h3>

                  <p style={styles.matchScore}>
                    Match Score:
                    <strong>
                      {" "}
                      {Math.round(job.match_score * 100)}%
                    </strong>
                  </p>

                  <p style={styles.reasoning}>
                    {job.reasoning}
                  </p>

                </div>

              ))}

            </div>

            {/* STRATEGIST */}

            <div style={styles.strategyCard}>

              <h2 style={styles.sectionTitle}>
                🧠 AI Career Strategist
              </h2>

              <p style={styles.strategyText}>
                {result.strategist.strategy}
              </p>

            </div>

            {/* SKILLS */}

            <div style={styles.skillsCard}>

              <h2 style={styles.sectionTitle}>
                🛠 Skills Intelligence
              </h2>

              <div style={styles.skillsGrid}>

                {result.skills.map((skill, i) => (

                  <div
                    key={i}
                    style={styles.skillBadge}
                  >
                    {skill}
                  </div>

                ))}

              </div>

            </div>

            {/* GAPS */}

            <div style={styles.gapsCard}>

              <h2 style={styles.sectionTitle}>
                ⚠️ Skill Gaps
              </h2>

              <div style={styles.skillsGrid}>

                {result.skill_gaps.map((gap, i) => (

                  <div
                    key={i}
                    style={styles.gapBadge}
                  >
                    {gap}
                  </div>

                ))}

              </div>

            </div>

            {/* LEARNING */}

            <div style={styles.learningCard}>

              <h2 style={styles.sectionTitle}>
                📚 Learning Roadmap
              </h2>

              <ul style={styles.learningList}>

                {result.learning_path.map((item, i) => (

                  <li
                    key={i}
                    style={styles.learningItem}
                  >
                    {item}
                  </li>

                ))}

              </ul>

            </div>

            {/* CAREER ADVICE */}

            <div style={styles.card}>

              <h2 style={styles.sectionTitle}>
                🚀 AI Career Advice
              </h2>

              <p style={styles.strategyText}>
                {result.career_advice}
              </p>

            </div>

          </div>

        )}

      </div>

    </div>
  );
}

const styles = {

  page: {
    backgroundColor: "#f3f6fb",
    minHeight: "100vh",
    padding: "30px",
  },

  container: {
    maxWidth: "1100px",
    margin: "auto",
    fontFamily: "Arial",
  },

  title: {
    textAlign: "center",
    fontSize: "52px",
    fontWeight: "800",
    marginBottom: "10px",
    color: "#111827",
  },

  subtitle: {
    textAlign: "center",
    color: "#4b5563",
    marginBottom: "35px",
    fontSize: "20px",
  },

  heroCard: {
    background: "linear-gradient(135deg, #2563eb, #06b6d4)",
    color: "white",
    padding: "30px",
    borderRadius: "20px",
    marginBottom: "30px",
    boxShadow: "0 10px 25px rgba(37,99,235,0.2)",
  },

  card: {
    background: "white",
    padding: "25px",
    borderRadius: "18px",
    marginBottom: "20px",
    boxShadow: "0 6px 18px rgba(0,0,0,0.08)",
  },

  jobCard: {
    background: "#dbeafe",
    padding: "25px",
    borderRadius: "18px",
    marginBottom: "20px",
    borderLeft: "8px solid #2563eb",
    boxShadow: "0 6px 18px rgba(37,99,235,0.15)",
    color: "#111827",
  },

  skillsCard: {
    background: "#dcfce7",
    padding: "25px",
    borderRadius: "18px",
    marginBottom: "20px",
    borderLeft: "8px solid #16a34a",
    boxShadow: "0 6px 18px rgba(22,163,74,0.15)",
    color: "#111827",
  },

  gapsCard: {
    background: "#fee2e2",
    padding: "25px",
    borderRadius: "18px",
    marginBottom: "20px",
    borderLeft: "8px solid #dc2626",
    boxShadow: "0 6px 18px rgba(220,38,38,0.15)",
    color: "#111827",
  },

  learningCard: {
    background: "#ffedd5",
    padding: "25px",
    borderRadius: "18px",
    marginBottom: "20px",
    borderLeft: "8px solid #ea580c",
    boxShadow: "0 6px 18px rgba(234,88,12,0.15)",
    color: "#111827",
  },

  readinessCard: {
    background: "#111827",
    color: "white",
    padding: "35px",
    borderRadius: "22px",
    marginBottom: "25px",
    textAlign: "center",
    boxShadow: "0 10px 25px rgba(0,0,0,0.2)",
  },

  strategyCard: {
    background: "#eef6ff",
    padding: "25px",
    borderRadius: "18px",
    marginBottom: "20px",
    borderLeft: "8px solid #0ea5e9",
    boxShadow: "0 6px 18px rgba(14,165,233,0.12)",
  },

  sectionTitle: {
    fontSize: "32px",
    fontWeight: "800",
    marginBottom: "20px",
    color: "#111827",
  },

  inputTitle: {
    fontSize: "28px",
    fontWeight: "700",
    color: "#111827",
    marginBottom: "20px",
  },

  readinessTitle: {
    fontSize: "36px",
    fontWeight: "800",
    marginBottom: "20px",
  },

  readinessLevel: {
    fontSize: "28px",
    fontWeight: "700",
    marginTop: "15px",
  },

  scoreCircle: {
    width: "140px",
    height: "140px",
    borderRadius: "50%",
    background: "#22c55e",
    margin: "25px auto",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: "36px",
    fontWeight: "800",
    boxShadow: "0 6px 18px rgba(34,197,94,0.3)",
  },

  progressBar: {
    width: "100%",
    height: "14px",
    background: "#374151",
    borderRadius: "10px",
    marginTop: "25px",
    overflow: "hidden",
  },

  progressFill: {
    height: "100%",
    background: "#22c55e",
  },

  label: {
    fontWeight: "700",
    display: "block",
    marginBottom: "10px",
    marginTop: "18px",
    color: "#111827",
  },

  textarea: {
    width: "100%",
    minHeight: "150px",
    padding: "14px",
    borderRadius: "12px",
    border: "1px solid #d1d5db",
    fontSize: "15px",
  },

  input: {
    width: "100%",
    padding: "14px",
    borderRadius: "12px",
    border: "1px solid #d1d5db",
    marginBottom: "20px",
    fontSize: "15px",
  },

  fileInput: {
    marginBottom: "15px",
  },

  button: {
    width: "100%",
    padding: "16px",
    border: "none",
    borderRadius: "12px",
    background: "#2563eb",
    color: "white",
    fontSize: "18px",
    cursor: "pointer",
    fontWeight: "700",
    boxShadow: "0 6px 18px rgba(37,99,235,0.25)",
  },

  reasoning: {
    color: "#1f2937",
    lineHeight: "1.8",
    fontWeight: "500",
    fontSize: "17px",
  },

  strategyText: {
    lineHeight: "2",
    color: "#1f2937",
    whiteSpace: "pre-line",
    fontSize: "17px",
  },

  skillsGrid: {
    display: "flex",
    flexWrap: "wrap",
    gap: "12px",
  },

  skillBadge: {
    background: "#bbf7d0",
    color: "#166534",
    padding: "10px 16px",
    borderRadius: "25px",
    fontWeight: "700",
    fontSize: "15px",
  },

  gapBadge: {
    background: "#fecaca",
    color: "#991b1b",
    padding: "10px 16px",
    borderRadius: "25px",
    fontWeight: "700",
    fontSize: "15px",
  },

  learningList: {
    paddingLeft: "20px",
  },

  learningItem: {
    marginBottom: "12px",
    fontSize: "17px",
    fontWeight: "600",
    color: "#7c2d12",
  },

  jobTitle: {
    fontSize: "28px",
    fontWeight: "800",
    color: "#1e3a8a",
    marginBottom: "10px",
  },

  matchScore: {
    fontSize: "20px",
    fontWeight: "600",
    color: "#111827",
    marginBottom: "15px",
  },

  resultsContainer: {
    marginTop: "35px",
  },

  orText: {
    textAlign: "center",
    margin: "18px 0",
    color: "#6b7280",
    fontWeight: "600",
  },
};

export default App;