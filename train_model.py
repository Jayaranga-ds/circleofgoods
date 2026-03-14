
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_excel("data/alumni_dataset_1000.xlsx")

# Features
X = data[["YearsExperience", "EngagementScore", "JobTitle", "Company"]]

# Target
y = data["Donated"]

# Define feature types
numeric_features = ["YearsExperience", "EngagementScore"]
categorical_features = ["JobTitle", "Company"]

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Full pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
    ]
)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "benefactor_model.pkl")

print("Model trained successfully and saved as benefactor_model.pkl")
