import os
import google.generativeai as genai

from app.llm.prompts import PLACEMENT_PROMPT

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_explanation(prediction, probability, student_data):

    prompt = PLACEMENT_PROMPT.format(
        cgpa=student_data["CGPA"],
        internships=student_data["Internships"],
        coding=student_data["Coding_Skills"],
        communication=student_data["Communication_Skills"],
        backlogs=student_data["Backlogs"],
        prediction=prediction,
        probability=probability
    )

    response = model.generate_content(prompt)

    return response.text