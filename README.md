# DoS Attack Binary Classifier Using CIC-IDS2017 Dataset

## Overview
We developed a machine learning classification pipeline including data preprocessing, feature engineering, exploratory analysis, model training, evaluation, and deployment. 

## Key Features
- Structured data preprocessing workflow
- Feature extraction for classification
- Model training and evaluation using scikit-learn
- Modular pipeline design

## Team Members & Roles
- **Emil Cacayan**: Manages GitHub repo and project, deployment, documentation (ADR), organization
- **Umar Siddiqui**: Modeling (simple models and train/test splitting, data preprocessing)
- **Nafisa Sabir**: ETL pipeline, construction of the deployment schema, data engineering 
- **Fnu Syed Moosa Aleem "Moosa"**: Modeling utilities, exploratory data analysis visualizations, evaluation

## Goal
The goal of this project is to evaluate different binary classifiers that distinguish DoS (denial of service) attacks from benign traffic in the CIC-IDS2017 dataset using Wednesday traffic, which contains the following labels:
- Benign
- DoS GoldenEye
- DoS Hulk
- DoS Slowhttptest
- DoS Slowloris
- Heartbleed (to be removed since this is not a DoS attack)

## Repo Structure
```
data: Data files as they get processed through the workflow
    raw: (contains original CSV/JSON/Parquet)
    interm: (contains preprocessed dataset)
    cleaned: (contains cleaned dataset)
etl: Contains code for extract, transform, load pipeline
eda: Contains code for exploratory data analysis
models: Contains code for models and saved weights/biases
deployment: Contains code for model deployment
notebooks: Contains rationale, documentation
adr: Contains the ADR for this project
```

## Usage
This repository contains analyses and performances of models trained to detect DoS traffic with associated annotations and deployed using FastAPI. The majority of the coding and corresponding output can be found in the subfolder `notebooks`, with each notebook organizing a step in the exploratory analysis, preprocessing, training, evaluation, and deployment process. The decision-making rationale for the design of this repository and project can be found in the `adr` folder. 

Raw Data Overview 

The raw dataset for Wednesday traffic is split into 12 separate files. These files come in three formats (CSV, JSON, and Parquet), but all of them share the exact same schema with 79 columns each. The only difference between them is how many rows each shard contains. After loading each file once and checking their shapes, the sizes are:

ids_0.csv → 1001 rows × 79 columns

ids_1.csv → 1001 rows × 79 columns

ids_2.csv → 1001 rows × 79 columns

ids_3.json → 1001 rows × 79 columns

ids_4.json → 1001 rows × 79 columns

ids_7.json → 9000 rows × 79 columns

ids_9.json → 10293 rows × 79 columns

ids_10.json → 5510 rows × 79 columns

ids_5.parquet → 15001 rows × 79 columns

ids_6.parquet → 5001 rows × 79 columns

ids_8.parquet → 10293 rows × 79 columns

ids_11.parquet → 1025 rows × 79 columns

## Summary
There are 12 raw files total. All of them use the same 79-feature structure, and only the number of rows varies across the shards. These files are the inputs that the ETL pipeline later combines and cleans.

## Using final_features.json for Model inference

The file **final_features.json** (located in data folder) contains the complete feature schema generated from the cleaned dataset (wednesday_cleaned.csv).
This schema is required during deployment to ensure that any incoming data is processed in the same way as the training data.

**How the Schema Is Used**
When the model receives new data (e.g., through FastAPI), the inference pipeline should:

1. Load the schema and the trained model.

2. Validate input data against the schema's defined columns and expected datatypes.

3. Reorder columns to match the schema’s feature ordering.

4. Cast column types according to the dtype definitions.

5. Apply numeric scaling using the stored statistics (mean, std) for each numeric feature.

6. Handle categorical features using the unique values defined in the schema.

7. Pass the transformed feature vector into the model for prediction.

**Example Usage Pattern**
import json
import pandas as pd

#Load schema
with open("data/final_features.json") as f:
    schema = json.load(f)

def apply_schema(df):
    # Validate required columns
    missing = set(schema.keys()) - {"_metadata"} - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Apply correct column order
    cols = [c for c in schema.keys() if c != "_metadata"]
    df = df[cols]

    # Cast datatypes
    for col in cols:
        df[col] = df[col].astype(schema[col]["dtype"])

    # Apply scaling to numeric features
    for col in cols:
        if schema[col]["feature_type"] == "numeric":
            mean = schema[col]["mean"]
            std = schema[col]["std"]
            df[col] = (df[col] - mean) / std

    return df

#Inference
X = apply_schema(new_input_df)
prediction = model.predict(X)

## Summary
The schema ensures that all inference requests follow the same preprocessing steps as the training pipeline.

By validating columns, enforcing ordering, casting types, and applying scaling from final_features.json, the model receives inputs in a stable and consistent format.
