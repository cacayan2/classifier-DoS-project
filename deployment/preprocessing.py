import json
import numpy as np
from pathlib import Path

class Preprocessor:
    def __init__(self, schema_path: str):
        """
        Instantiator method for the preprocessor class. 
        
        :param self: This object.
        :param schema_path: The path to the final_features.json file.
        """
        self.schema_path = Path(schema_path)

        # First we need to load the schema
        with open(self.schema_path, "r") as f:
            schema = json.load(f)
        
        # Then we need to extract the scaler parameters from final_features.json
        scaler_params = schema["scaler_params"]

        self.feature_names = scaler_params["feature_names"]
        self.feature_means = np.array(scaler_params["feature_means"], dtype = float)
        self.feature_stds = np.array(scaler_params["feature_stds"], dtype = float)

        # Convert the numeric types to a dictionary for faster lookup. 
        self.numeric_types = {
            k: v["dtype"]
            for k, v in self.schema.items()
            if isinstance(v, dict) and v.get("feature_type") == "numeric"
        }
        
        self.n_features = len(self.feature_names)

    def validate_input(self, sample: dict):
        # Sanity check to ensure the feature names, means, and stds are the same length
        if len(self.feature_names) != len(self.feature_means) or len(self.feature_names) != len(self.feature_stds):
            raise ValueError("Feature names, means, and stds are not the same length")

        # Check for missing fields. 
        for f in self.features:
            if not f in sample:
                raise ValueError(f"Missing feature {f}")
        
        # Check for unexpected fields.
        for k in sample.keys():
            if k not in self.features:
                raise ValueError(f"Unexpected feature {k}")
        
        # Validate the numeric types.
        for key, expected_type in self.numeric_types.items():
            value = sample[key]
            
            # Raise exception if the value is null.
            if value is None:
                raise ValueError(f"Field '{key}' cannot be null.")
            
            # Try to typecast the value to numeric, otherwise raise exception.
            if not isinstance(value, (int, float)):
                try:
                    sample[key] = float(value)
                except:
                    raise ValueError(f"Field '{key}' must be numeric, but value is '{value}' with type {type(value)}.")
                
        return sample
    
    def safe_scaling(self, X):
        """
        Safely scales the dataset by avoiding divide by zero errors.
        
        :param self: This object.
        :param X: The dataset to be scaled (numpy array). 
        """
        # If the std is too small, replace it with 1.0
        safe_stds = np.where(self.stds < 1e-12, 1.0, self.stds)

        # Apply the scaling.
        return (X - self.means) / safe_stds

    def preprocess_input(self, sample: dict):
        """
        Takes a dictionary containing raw feature inputs
        and returns a (1, n_features) scaled numpy array. 

        Missing features are filled with 0.0.
        
        :param self: This object.
        :param sample: The dictionary containing raw feature inputs.
        """
        # First validate the input
        sample = self.validate(sample)

        # Then order the features.
        ordered = [sample[f] for f in self.features]

        # Then we convert to a dataframe and scale and reshape the array for prediction.
        X = np.array(ordered, dtype = float).reshape(1, -1)
        
        # Apply scaling.
        X_scaled = self.scale(X)

        return X_scaled