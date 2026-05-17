import joblib
import pandas as pd


# =========================
# Load Model + Scaler
# =========================

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

    # Ensure exact column order
    features_df = data[FEATURE_COLUMNS]

    # Scale features
    scaled_features = scaler.transform(features_df)

    # Prediction
    prediction = model.predict(scaled_features)[0]

    probability = model.predict_proba(scaled_features)[0][1]

    return {
        "prediction": "Placed" if prediction == 1 else "Not Placed",
        "probability": round(float(probability), 4)
    }

    # -------------------------
    # Convert to DataFrame
    # -------------------------

    features_df = pd.DataFrame([input_data])

    # Exact column order
    features_df = features_df[FEATURE_COLUMNS]

    # -------------------------
    # Scale Features
    # -------------------------

    scaled_features = scaler.transform(features_df)

    # -------------------------
    # Prediction
    # -------------------------

    prediction = model.predict(scaled_features)[0]

    probability = model.predict_proba(scaled_features)[0][1]

    # -------------------------
    # Return Result
    # -------------------------

    return {
        "prediction": "Placed" if prediction == 1 else "Not Placed",
        "probability": round(float(probability), 4)
    }