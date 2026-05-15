from pydantic import BaseModel

class StudentData(BaseModel):
    CGPA: float
    Coding_Skills: int
    Communication_Skills: int
    Internships: int
    Backlogs: int
    Age: int
    Gender: str
    Degree: str
    Branch: str