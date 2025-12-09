from fastapi import FastAPI
import joblib
import json
from pathlib import Path

from deployment.schema_loader import load_schema
from deployment.preprocessing import preprocess_input

# First we create a new FastAPI object
app = FastAPI(
    title = "DoS Classifier API",
    version = "0.1.0",
    description = "API for predicting DoS attacks vs. benign traffic"
)

# Load the schema
SCHEMA_PATH = Path("data/final_features.json")
schema = load_schema(SCHEMA_PATH)

# Load the trained model
MODEL_PATH = Path("models/saved_model/random_forest.pkl")

# This logic is required because as of the writing of this code, no model has been trained. 
if MODEL_PATH.exists():
    model = joblib.load(MODEL_PATH)
else:
    model = None

# Implementation of health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Implementation of version endpoint
@app.get("/version")
def version():
    return {"api_version": "0.1.0"}

# Implementation of prediction endpoint (inference not yet implemented)
@app.post("/predict")
def predict(input_data: dict):
    if model is None:
        return {"error": "Model is not available - please train"}
    
    # Preprocess input data
    processed = preprocess_input(input_data, schema)
    prediction = model.predict([processed])[0]
    return {"prediction": int(prediction)}