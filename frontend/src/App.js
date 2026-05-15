import { useState } from "react";
import axios from "axios";

function App() {

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

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const predict = async () => {
    setLoading(true);
  try {
    const cleanedForm = {
      ...form,
      Age: Number(form.Age),
      CGPA: Number(form.CGPA),
      Internships: Number(form.Internships),
      Coding_Skills: Number(form.Coding_Skills),
      Communication_Skills: Number(form.Communication_Skills),
      Backlogs: Number(form.Backlogs)
    };

    const res = await axios.post(
      "https://aispry-placement-prediction.onrender.com/predict",
      cleanedForm
    );
    console.log("API RESPONSE:", res.data);
    setResult(res.data);
    setLoading(false);

  } catch (error){
    console.log("ERROR:", error.response?.data || error.message);
    setLoading(false);  
  }
};

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>

      <h2>AI Placement Prediction</h2>

      <input type="number" name="Age" placeholder="Age" onChange={handleChange} />
      <input type="number" name="CGPA" placeholder="CGPA" onChange={handleChange} />
      <input name="Internships" placeholder="Internships" onChange={handleChange} />
      <input name="Coding_Skills" placeholder="Coding Skills" onChange={handleChange} />
      <input name="Communication_Skills" placeholder="Communication Skills" onChange={handleChange} />
      <input name="Backlogs" placeholder="Backlogs" onChange={handleChange} />

      <select name="Gender" onChange={handleChange}>
  <option value="">Select Gender</option>
  <option value="Male">Male</option>
  <option value="Female">Female</option>
</select>
      <select name="Degree" onChange={handleChange}>
  <option value="">Select Degree</option>
  <option value="B.Tech">B.Tech</option>
  <option value="BCA">BCA</option>
  <option value="MCA">MCA</option>
</select>
      <select name="Branch" onChange={handleChange}>
  <option value="">Select Branch</option>
  <option value="ECE">ECE</option>
  <option value="IT">IT</option>
  <option value="ME">ME</option>
  <option value="Civil">Civil</option>
</select>

      <br /><br />

      <button onClick={predict}>
        Predict Placement
      </button>
      {loading && <p>Predicting...</p>}
      {result && (
  <div style={{
    marginTop: "20px",
    padding: "15px",
    border: "1px solid #ccc",
    borderRadius: "10px",
    width: "300px"
  }}>
    <h3>Prediction: {result.prediction}</h3>
  </div>
)}

    </div>
  );
}

export default App;