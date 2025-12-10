from fastapi import FastAPI, HTTPException
import joblib
import json
from pathlib import Path

from deployment.schema_loader import load_schema
from deployment.preprocessing import Preprocessor

# First we create a new FastAPI object
app = FastAPI(
    title = "DoS Classifier API",
    version = "0.1.0",
    description = "API for predicting DoS attacks vs. benign traffic"
)

# Load the schema
SCHEMA_PATH = Path("data/final_features.json")
schema = load_schema(SCHEMA_PATH)

# Then we create the preprocessor object.
preprocessor = Preprocessor(schema_path = SCHEMA_PATH)

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
    # Running preprocessing with sanity checking.
    try:
        X = preprocessor.preprocess_input(input_data)
    except Exception as e:
        raise HTTPException(
            status_code = 400, 
            detail = f"Failed to preprocess input data: {e}"
        )
    try:
        y_pred = model.predict(X)
    except Exception as e:
        raise HTTPException(
            status_code = 500, 
            detail = f"Failed to make predictions: {e}"
        )
    return {"prediction": int(y_pred[0])}