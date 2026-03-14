
import pandas as pd
import joblib
import os


# Ensure outputs folder exists
os.makedirs("outputs", exist_ok=True)


# Load trained model
model = joblib.load("outputs/benefactor_model.pkl")


# Load alumni dataset
data = pd.read_excel("data/alumni_dataset_1000.xlsx")


# Select features used during training
features = data[
    [
        "College",
        "Degree",
        "Company",
        "JobTitle",
        "Skills",
        "YearsExperience",
        "EngagementScore",
    ]
]


# Predict donation probability
probabilities = model.predict_proba(features)[:, 1]


# Add predictions to dataset
data["DonationProbability"] = probabilities


# Sort alumni by highest probability
ranked = data.sort_values(by="DonationProbability", ascending=False)


# Save results
output_path = "outputs/alumni_benefactor_ranking.xlsx"
ranked.to_excel(output_path, index=False)


print("Prediction completed successfully!")
print("Results saved to:", output_path)
