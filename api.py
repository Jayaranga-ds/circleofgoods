from fastapi import FastAPI
import pandas as pd
import subprocess

app = FastAPI(title="Circle of Good ML API")


# Home route
@app.get("/")
def home():
    return {"message": "Circle of Good ML API running"}


# Run the ML pipeline
@app.post("/run-pipeline")
def run_pipeline():

    subprocess.run(["python", "pipeline.py"])

    return {"status": "Pipeline executed successfully"}


# Get mentor recommendations
@app.get("/mentor-recommendations")
def get_mentor_recommendations():

    df = pd.read_excel("outputs/mentor_student_recommendations.xlsx")

    return df.to_dict(orient="records")


# Get benefactor predictions
@app.get("/benefactor-ranking")
def get_benefactor_ranking():

    df = pd.read_excel("outputs/alumni_benefactor_ranking.xlsx")

    return df.to_dict(orient="records")


# Get helping score
@app.get("/helping-score")
def get_helping_score():

    df = pd.read_excel("outputs/alumni_helping_score.xlsx")

    return df.to_dict(orient="records")