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

        {/* ABOUT */}

        <div style={styles.heroCard}>

          <h2>🧠 AI-Powered Career Strategy</h2>

          <p>
            OrchestrAI uses multiple AI agents to analyze CVs,
            match career opportunities, identify skill gaps,
            and generate intelligent career strategies.
          </p>

        </div>

        {/* INPUT SECTION */}

        <div style={styles.card}>

          <h3>📄 CV Input</h3>

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

              <h2>🎯 Career Readiness</h2>

              <div style={styles.scoreCircle}>
                {result.strategist.readiness_score}%
              </div>

              <h3>
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

            <div style={styles.card}>

              <h2>💼 Job Match</h2>

              {result.matched_jobs.map((job, i) => (

                <div key={i}>

                  <h3>
                    {job.job_title}
                  </h3>

                  <p>
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

              <h2>🧠 AI Career Strategist</h2>

              <p style={styles.strategyText}>
                {result.strategist.strategy}
              </p>

            </div>

            {/* SKILLS */}

            <div style={styles.card}>

              <h2>🛠 Skills Intelligence</h2>

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

            <div style={styles.card}>

              <h2>⚠️ Skill Gaps</h2>

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

            <div style={styles.card}>

              <h2>📚 Learning Roadmap</h2>

              <ul>

                {result.learning_path.map((item, i) => (

                  <li key={i}>
                    {item}
                  </li>

                ))}

              </ul>

            </div>

            {/* CAREER ADVICE */}

            <div style={styles.card}>

              <h2>🚀 AI Career Advice</h2>

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
    backgroundColor: "#f4f7fb",
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
    fontSize: "48px",
    marginBottom: "10px",
  },

  subtitle: {
    textAlign: "center",
    color: "#666",
    marginBottom: "30px",
    fontSize: "18px",
  },

  heroCard: {
    background: "linear-gradient(135deg, #4CAF50, #2196F3)",
    color: "white",
    padding: "25px",
    borderRadius: "15px",
    marginBottom: "25px",
  },

  card: {
    background: "white",
    padding: "20px",
    borderRadius: "15px",
    marginBottom: "20px",
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
  },

  readinessCard: {
    background: "#111827",
    color: "white",
    padding: "30px",
    borderRadius: "20px",
    marginBottom: "20px",
    textAlign: "center",
  },

  strategyCard: {
    background: "#eef6ff",
    padding: "25px",
    borderRadius: "15px",
    marginBottom: "20px",
    borderLeft: "6px solid #2196F3",
  },

  scoreCircle: {
    width: "130px",
    height: "130px",
    borderRadius: "50%",
    background: "#4CAF50",
    margin: "20px auto",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: "32px",
    fontWeight: "bold",
  },

  progressBar: {
    width: "100%",
    height: "12px",
    background: "#374151",
    borderRadius: "10px",
    marginTop: "20px",
    overflow: "hidden",
  },

  progressFill: {
    height: "100%",
    background: "#4CAF50",
  },

  label: {
    fontWeight: "bold",
    display: "block",
    marginBottom: "8px",
    marginTop: "15px",
  },

  textarea: {
    width: "100%",
    minHeight: "140px",
    padding: "12px",
    borderRadius: "10px",
    border: "1px solid #ccc",
  },

  input: {
    width: "100%",
    padding: "12px",
    borderRadius: "10px",
    border: "1px solid #ccc",
    marginBottom: "20px",
  },

  fileInput: {
    marginBottom: "15px",
  },

  button: {
    width: "100%",
    padding: "14px",
    border: "none",
    borderRadius: "10px",
    background: "#4CAF50",
    color: "white",
    fontSize: "18px",
    cursor: "pointer",
    fontWeight: "bold",
  },

  reasoning: {
    color: "#555",
    lineHeight: "1.6",
  },

  strategyText: {
    lineHeight: "1.8",
    color: "#333",
    whiteSpace: "pre-line",
  },

  skillsGrid: {
    display: "flex",
    flexWrap: "wrap",
    gap: "10px",
  },

  skillBadge: {
    background: "#dbeafe",
    color: "#1e40af",
    padding: "8px 14px",
    borderRadius: "20px",
    fontWeight: "bold",
  },

  gapBadge: {
    background: "#fee2e2",
    color: "#991b1b",
    padding: "8px 14px",
    borderRadius: "20px",
    fontWeight: "bold",
  },

  resultsContainer: {
    marginTop: "30px",
  },

  orText: {
    textAlign: "center",
    margin: "15px 0",
    color: "#666",
  },
};

export default App;