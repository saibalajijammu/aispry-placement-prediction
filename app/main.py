from fastapi import FastAPI


from app.schema import StudentData
from app.utils import predict_placement
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="AI Placement Prediction API",
    description="Predict student placement status",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Placement Prediction API Running"}

@app.post("/predict")
def predict(data: StudentData):

    result = predict_placement(data)

    return {
        "prediction": result
    }