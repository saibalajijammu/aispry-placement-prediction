import google.generativeai as genai

genai.configure(api_key="AIzaSyDYITrFV1ePvIjnqGKd3io8b-Q1SlBtHHI")

models = genai.list_models()

for model in models:
    print(model.name)