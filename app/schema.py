

from pydantic import BaseModel

class StudentIDRequest(BaseModel):
    student_id: int


class ManualPredictionRequest(BaseModel):
    Age: int
    CGPA: float
    Internships: int
    Coding_Skills: int
    Communication_Skills: int
    Backlogs: int
    Gender: str
    Degree: str
    Branch: str