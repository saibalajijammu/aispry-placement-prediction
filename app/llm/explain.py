import os
import google.generativeai as genai

from app.llm.prompts import PLACEMENT_PROMPT


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_explanation(features, prediction):

    prompt = PLACEMENT_PROMPT.format(
        cgpa=features["CGPA"][0],
        internships=features["Internships"][0],
        coding=features["Coding_Skills"][0],
        communication=features["Communication_Skills"][0],
        backlogs=features["Backlogs"][0],
        prediction=prediction
    )

    response = model.generate_content(prompt)

    return response.text