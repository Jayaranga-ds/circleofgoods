
import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Ensure outputs folder exists
os.makedirs("outputs", exist_ok=True)


# Load alumni dataset
data = pd.read_excel("data/alumni_dataset_1000.xlsx")


# Select features
X = data[
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

# Target column
y = data["Donated"]


# Numerical columns
numeric_features = ["YearsExperience", "EngagementScore"]

# Text columns
categorical_features = [
    "College",
    "Degree",
    "Company",
    "JobTitle",
    "Skills",
]


# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ]
)


# ML pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=150, random_state=42)),
    ]
)


# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Train model
model.fit(X_train, y_train)


# Evaluate
pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)


# Save trained model
joblib.dump(model, "outputs/benefactor_model.pkl")


# Save metrics
with open("outputs/model_metrics.txt", "w") as f:
    f.write(f"Model Accuracy: {accuracy}\n")


print("Model trained successfully")
print("Accuracy:", accuracy)
print("Model saved to outputs/benefactor_model.pkl")
