from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model once when API starts

model = joblib.load("benefactor_model.pkl")

# Home route

@app.get("/")
def home():
    return {"message": "Benefactor Prediction API Running"}

# Single prediction

@app.post("/predict")
def predict(years_experience: int, engagement_score: int, career_length: int):

    data = pd.DataFrame({
    "YearsExperience": [years_experience],
    "EngagementScore": [engagement_score],
    "CareerLength": [career_length]
    })

    prediction = model.predict_proba(data)
    probability = prediction[0][1]

    return {"donation_probability": float(probability)}

# Batch prediction

@app.post("/predict_batch")
def predict_batch(alumni_list: list):


    df = pd.DataFrame(alumni_list)

    predictions = model.predict_proba(df)

    results = []

    for i, prob in enumerate(predictions):
        results.append({
        "alumni_index": i,
        "donation_probability": float(prob[1])
         })

    return {"results": results}

