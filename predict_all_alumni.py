import pandas as pd
import joblib

def predict_all_alumni():


# Load trained model
    model = joblib.load("benefactor_model.pkl")

# Load alumni dataset
    data = pd.read_excel("data/alumni_dataset_1000.xlsx")

# Create CareerLength column if missing
    data["CareerLength"] = data["YearsExperience"]

# Select features used for prediction
    features = data[["YearsExperience", "EngagementScore", "CareerLength"]]

# Predict donation probability
    data["DonationProbability"] = model.predict_proba(features)[:, 1]

# Save results
    data.to_excel("outputs/alumni_benefactor_ranking.xlsx", index=False)

    print("Alumni prediction completed!")

if __name__== "__main__":
    predict_all_alumni()
