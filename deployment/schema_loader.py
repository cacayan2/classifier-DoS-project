import json
from pathlib import Path

def load_schema(schema_path: Path):
    """
    Loads the project's `final_features.json` schema.

    :param schema_path: Path to the schema file.
    """
    schema_path = Path(schema_path)

    # Check if the schema_path exists.
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found at {schema_path}")

    with open(schema_path, "r") as f:
        schema = json.load(f)

    # Added sanity checking to ensure all keys are present.
    required_sections = ["scaler_params", "_metadata"]
    for section in required_sections:
        if section not in schema:
            raise KeyError(f"Required section '{section}' not found in schema")

    # Validating if length of scaling arrays match length of feature list.
    scaler = schema["scaler_params"]
    if not (len(scaler["feature_names"]) == len(scaler["feature_means"]) == len(scaler["feature_stds"])):
        raise ValueError("Length of scaling arrays does not match length of feature list")

    return schema