from schema import StudentData

print(StudentData.model_json_schema())


import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from schema import StudentData
from utils import predict_placement
from feast_utils import get_student_features
from fastapi.openapi.utils import get_openapi


app = FastAPI(
    title="AI Placement Prediction API",
    description="Predict student placement status",
    version="1.0"
)

Instrumentator().instrument(app).expose(app)

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


@app.post("/predict")
def predict(data: StudentData):

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

    return result


@app.get("/student/{student_id}")
def fetch_student(student_id: int):

    features = get_student_features(student_id)

    return features

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi