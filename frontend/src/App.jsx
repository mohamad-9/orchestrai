import { useState } from "react";

function App() {
  const [cvText, setCvText] = useState("");
  const [targetRole, setTargetRole] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState(null);

  // ✅ API URL from environment
  const API_URL = import.meta.env.VITE_API_URL;

  const handleAnalyze = async () => {
    setLoading(true);

    try {
      let response;

      if (file) {
        const formData = new FormData();
        formData.append("file", file);
        formData.append("target_role", targetRole);

        // ✅ FIXED HERE
        response = await fetch(`${API_URL}/analyze-pdf`, {
          method: "POST",
          body: formData,
        });

      } else {
        // ✅ FIXED HERE
        response = await fetch(`${API_URL}/analyze`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            cv_text: cvText,
            target_role: targetRole,
            user_id: "demo_user",
          }),
        });
      }

      const data = await response.json();
      setResult(data);

    } catch (error) {
      console.error("Error:", error);
    }

    setLoading(false);
  };

  return (
    <div style={styles.container}>
      
      <h1 style={styles.title}>OrchestrAI 🚀</h1>
      <p style={styles.subtitle}>
        Multi-Agent AI Career Assistant
      </p>

      <div style={styles.aboutBox}>
        <h3>💡 What is OrchestrAI?</h3>
        <p>
          Analyze your CV using AI agents to match jobs, detect skill gaps,
          and generate a personalized learning path.
        </p>
      </div>

      <label>Paste your CV</label>
      <textarea
        placeholder="Paste your CV here..."
        value={cvText}
        onChange={(e) => {
          setCvText(e.target.value);
          if (e.target.value) setFile(null);
        }}
        style={styles.textarea}
        disabled={file !== null}
      />

      <p style={{ textAlign: "center", margin: "10px 0" }}>— OR —</p>

      <label>Upload CV (PDF)</label>
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => {
          setFile(e.target.files[0]);
          if (e.target.files[0]) setCvText("");
        }}
        style={{ marginBottom: "10px" }}
        disabled={cvText.length > 0}
      />

      <input
        placeholder="Target Role (e.g. AI Engineer)"
        value={targetRole}
        onChange={(e) => setTargetRole(e.target.value)}
        style={styles.input}
      />

      <button onClick={handleAnalyze} style={styles.button}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {result && (
        <div style={styles.results}>
          
          <div style={styles.card}>
            <h3>🧠 Skills</h3>
            <ul>
              {result.skills.map((s, i) => (
                <li key={i}>{s}</li>
              ))}
            </ul>
          </div>

          <div style={styles.card}>
            <h3>💼 Job Match</h3>
            {result.matched_jobs.map((job, i) => (
              <div key={i}>
                <p><strong>{job.job_title}</strong></p>
                <p>Score: {job.match_score}</p>
                <p style={{ color: "#555" }}>{job.reasoning}</p>
              </div>
            ))}
          </div>

          <div style={styles.card}>
            <h3>⚠️ Skill Gaps</h3>
            <ul>
              {result.skill_gaps.map((s, i) => (
                <li key={i}>{s}</li>
              ))}
            </ul>
          </div>

          <div style={styles.card}>
            <h3>📚 Learning Path</h3>
            <ul>
              {result.learning_path.map((l, i) => (
                <li key={i}>{l}</li>
              ))}
            </ul>
          </div>

        </div>
      )}
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "900px",
    margin: "auto",
    padding: "20px",
    fontFamily: "Arial",
  },
  title: {
    textAlign: "center",
  },
  subtitle: {
    textAlign: "center",
    color: "#777",
    marginBottom: "20px",
  },
  aboutBox: {
    background: "#eef6ff",
    padding: "15px",
    borderRadius: "10px",
    marginBottom: "20px",
  },
  textarea: {
    width: "100%",
    height: "120px",
    marginBottom: "10px",
    padding: "10px",
  },
  input: {
    width: "100%",
    marginBottom: "10px",
    padding: "10px",
  },
  button: {
    width: "100%",
    padding: "12px",
    backgroundColor: "#4CAF50",
    color: "white",
    border: "none",
    cursor: "pointer",
    fontSize: "16px",
  },
  results: {
    marginTop: "20px",
  },
  card: {
    background: "#f9f9f9",
    padding: "15px",
    marginBottom: "15px",
    borderRadius: "10px",
    boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
  },
};

export default App;