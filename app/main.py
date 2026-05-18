

import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from app.schema import StudentIDRequest, ManualPredictionRequest
from app.utils import predict_placement
from app.feast_utils import get_student_features
from dotenv import load_dotenv
from app.llm.explain import generate_explanation

load_dotenv()   


app = FastAPI(
    title="AI Placement Prediction API",
    description="Predict student placement status",
    version="1.0"
)

Instrumentator().instrument(app).expose(app)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Placement Prediction API Running"
    }


@app.post("/predict2")
def predict(data: StudentIDRequest):

    features = get_student_features(
        data.student_id
    )

    input_data = {
        "Age": features["Age"][0],
        "CGPA": features["CGPA"][0],
        "Internships": features["Internships"][0],
        "Coding_Skills": features["Coding_Skills"][0],
        "Communication_Skills": features["Communication_Skills"][0],
        "Backlogs": features["Backlogs"][0],

        "Gender": features["Gender"][0],

        "Degree_B.Tech": features["Degree_B.Tech"][0],
        "Degree_BCA": features["Degree_BCA"][0],
        "Degree_MCA": features["Degree_MCA"][0],

        "Branch_Civil": features["Branch_Civil"][0],
        "Branch_ECE": features["Branch_ECE"][0],
        "Branch_IT": features["Branch_IT"][0],
        "Branch_ME": features["Branch_ME"][0],
    }

    df = pd.DataFrame([input_data])

    result = predict_placement(df)

    prediction_value = (
    "Placed"
    if result["prediction"] == 1
    else "Not Placed"
)

    explanation = generate_explanation(
    prediction=result["prediction"],
    probability=result["probability"],
    student_data=df.iloc[0].to_dict()
)

    return {
    "prediction": prediction_value,
    "probability": result.get("probability"),
    "explanation": explanation
}

@app.post("/predict")
def predict_manual(data: ManualPredictionRequest):

    raw_df = pd.DataFrame([data.dict()])

    df = pd.get_dummies(raw_df)

    expected_cols = [
        'Age',
        'CGPA',
        'Internships',
        'Coding_Skills',
        'Communication_Skills',
        'Backlogs',
        'Gender_Male',
        'Degree_B.Tech',
        'Degree_BCA',
        'Degree_MCA',
        'Branch_Civil',
        'Branch_ECE',
        'Branch_IT',
        'Branch_ME'
    ]

    for col in expected_cols:
        if col not in df.columns:
            df[col] = 0

    df = df[expected_cols]

    result = predict_placement(df)

    prediction_value = (
        "Placed"
        if result["prediction"] == 1
        else "Not Placed"
    )

    explanation = generate_explanation(
        features={
            "CGPA": [data.CGPA],
            "Internships": [data.Internships],
            "Coding_Skills": [data.Coding_Skills],
            "Communication_Skills": [data.Communication_Skills],
            "Backlogs": [data.Backlogs]
        },
        prediction=prediction_value
    )

    return {
        "prediction": prediction_value,
        "probability": result["probability"],
        "explanation": explanation
    }


@app.get("/student/{student_id}")
def fetch_student(student_id: int):

    features = get_student_features(student_id)

    return features

