import { useState } from "react";
import axios from "axios";

function App() {

  // -------------------------
  // Mode Toggle
  // -------------------------

  const [useStudentId, setUseStudentId] = useState(true);

  // -------------------------
  // Student ID
  // -------------------------

  const [studentId, setStudentId] = useState("");

  // -------------------------
  // Manual Form
  // -------------------------

  const [form, setForm] = useState({
    Age: 21,
    CGPA: 8,
    Internships: 1,
    Coding_Skills: 7,
    Communication_Skills: 7,
    Backlogs: 0,
    Gender: "Male",
    Degree: "B.Tech",
    Branch: "ECE"
  });

  // -------------------------
  // Result
  // -------------------------

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // -------------------------
  // Handle Input Change
  // -------------------------

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  // -------------------------
  // Predict Function
  // -------------------------

  const predict = async () => {

    setLoading(true);

    try {

      let payload = {};

      // =========================
      // Existing Student
      // =========================

      if (useStudentId) {

        payload = {
          student_id: Number(studentId)
        };

      }

      // =========================
      // New User Manual Entry
      // =========================

      else {

        payload = {
          ...form,
          Age: Number(form.Age),
          CGPA: Number(form.CGPA),
          Internships: Number(form.Internships),
          Coding_Skills: Number(form.Coding_Skills),
          Communication_Skills: Number(form.Communication_Skills),
          Backlogs: Number(form.Backlogs)
        };

      }

      // =========================
      // API CALL
      // =========================

      const endpoint = useStudentId
  ? "https://aispry-placement-prediction.onrender.com/predict2"
  : "https://aispry-placement-prediction.onrender.com/predict";

      const res = await axios.post(
  endpoint,
  payload,
  {
    timeout: 120000
  }
);

      console.log("API DATA:",res.data);

      setResult(res.data);

    } catch (error) {

  console.log("FULL ERROR:", error);

  alert(
    JSON.stringify(
      error.response?.data || error.message,
      null,
      2
    )
  );

}

    setLoading(false);
  };

  return (

    <div style={{
      padding: "20px",
      fontFamily: "Arial",
      maxWidth: "700px",
      margin: "auto"
    }}>

      <h1>AI Placement Prediction</h1>

      {/* ========================= */}
      {/* TOGGLE */}
      {/* ========================= */}

      <div style={{ marginBottom: "20px" }}>

        <button
          onClick={() => setUseStudentId(true)}
          style={{
            marginRight: "10px",
            padding: "10px"
          }}
        >
          Existing Student
        </button>

        <button
          onClick={() => setUseStudentId(false)}
          style={{
            padding: "10px"
          }}
        >
          New User
        </button>

      </div>

      {/* ========================= */}
      {/* STUDENT ID SECTION */}
      {/* ========================= */}

      {useStudentId ? (

        <div>

          <input
            type="number"
            placeholder="Enter Student ID"
            value={studentId}
            onChange={(e) => setStudentId(e.target.value)}
            style={{
              width: "300px",
              padding: "10px"
            }}
          />

        </div>

      ) : (

        /* ========================= */
        /* MANUAL FORM */
        /* ========================= */

        <div style={{
          display: "flex",
          flexDirection: "column",
          gap: "10px"
        }}>

          <input type="number" name="Age" placeholder="Age" value={form.Age} onChange={handleChange} />

          <input type="number" step="0.1" name="CGPA" placeholder="CGPA" value={form.CGPA} onChange={handleChange} />

          <input type="number" name="Internships" placeholder="Internships" value={form.Internships} onChange={handleChange} />

          <input type="number" name="Coding_Skills" placeholder="Coding Skills" value={form.Coding_Skills} onChange={handleChange} />

          <input type="number" name="Communication_Skills" placeholder="Communication Skills" value={form.Communication_Skills} onChange={handleChange} />

          <input type="number" name="Backlogs" placeholder="Backlogs" value={form.Backlogs} onChange={handleChange} />

          {/* Gender */}

          <select name="Gender" onChange={handleChange}>
            <option value="">Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>

          {/* Degree */}

          <select name="Degree" onChange={handleChange}>
            <option value="">Select Degree</option>
            <option value="B.Tech">B.Tech</option>
            <option value="BCA">BCA</option>
            <option value="MCA">MCA</option>
          </select>

          {/* Branch */}

          <select name="Branch" onChange={handleChange}>
            <option value="">Select Branch</option>
            <option value="ECE">ECE</option>
            <option value="IT">IT</option>
            <option value="ME">ME</option>
            <option value="Civil">Civil</option>
          </select>

        </div>

      )}

      {/* ========================= */}
      {/* BUTTON */}
      {/* ========================= */}

      <br />

      <button
        onClick={predict}
        style={{
          padding: "12px 20px",
          fontSize: "16px"
        }}
      >
        Predict Placement
      </button>

      {/* ========================= */}
      {/* LOADING */}
      {/* ========================= */}

      {loading && <p>Predicting...</p>}

      {/* ========================= */}
      {/* RESULT */}
      {/* ========================= */}

      {result && (

        <div style={{
          marginTop: "30px",
          padding: "20px",
          border: "1px solid #ccc",
          borderRadius: "10px"
        }}>

          <h2>Prediction: {result.prediction}</h2>

          <h3>
            Probability: {(result.probability * 100).toFixed(2)}%
          </h3>

          <hr />

          <h3>AI Career Guidance</h3>

          <p style={{
            whiteSpace: "pre-line",
            lineHeight: "1.7"
          }}>
            {result.explanation}
          </p>

        </div>

      )}

    </div>
  );
}

export default App;