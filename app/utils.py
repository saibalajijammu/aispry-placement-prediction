import joblib
import pandas as pd


model = joblib.load("models/best_model.pkl") 
scaler = joblib.load("models/scaler.pkl") 

# =========================
# Feature Columns
# MUST match training order exactly
# =========================

FEATURE_COLUMNS = [
    "Age",
    "Gender",
    "CGPA",
    "Internships",
    "Coding_Skills",
    "Communication_Skills",
    "Backlogs",
    "Degree_B.Tech",
    "Degree_BCA",
    "Degree_MCA",
    "Branch_Civil",
    "Branch_ECE",
    "Branch_IT",
    "Branch_ME"
]

# =========================
# Prediction Function
# =========================

def predict_placement(data):

    # -------------------------
    # One-hot encoding manually
    # -------------------------

    input_data = {
        "Age": data.Age,
        "CGPA": data.CGPA,
        "Internships": data.Internships,
        "Coding_Skills": data.Coding_Skills,
        "Communication_Skills": data.Communication_Skills,
        "Backlogs": data.Backlogs,

        # Gender
        "Gender": 1 if data.Gender.lower() == "male" else 0,

        # Degree
        "Degree_B.Tech": 1 if data.Degree == "B.Tech" else 0,
        "Degree_BCA": 1 if data.Degree == "BCA" else 0,
        "Degree_MCA": 1 if data.Degree == "MCA" else 0,

        # Branch
        "Branch_Civil": 1 if data.Branch == "Civil" else 0,
        "Branch_ECE": 1 if data.Branch == "ECE" else 0,
        "Branch_IT": 1 if data.Branch == "IT" else 0,
        "Branch_ME": 1 if data.Branch == "ME" else 0
    }

    # -------------------------
    # Convert to DataFrame
    # -------------------------

    features_df = pd.DataFrame([input_data])

    # Ensure exact column order
    features_df = features_df[FEATURE_COLUMNS]

    # -------------------------
    # Scale Features
    # -------------------------

    scaled_features = scaler.transform(features_df)

    # -------------------------
    # Prediction
    # -------------------------

    prediction = model.predict(scaled_features)[0]

    

    # -------------------------
    # Return Result
    # -------------------------

    return "Placed" if prediction == 1 else "Not Placed"