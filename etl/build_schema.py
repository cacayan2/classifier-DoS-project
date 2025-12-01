def build_schema(input_path, output_path):
    """
    Build a schema from the cleaned dataset.

    Args:
        input_path: Path to cleaned CSV file
        output_path: Path to save the schema JSON

    Returns:
        Dictionary containing the schema
    """
    # Read the cleaned dataset
    print(f"Reading data from: {input_path}")
    df = pd.read_csv(input_path)

    schema = {}

    # Iterate through each column
    for col in df.columns:
        col_info = {}

        # Get data type
        col_info['dtype'] = str(df[col].dtype)

        # Determine if numeric or categorical
        if pd.api.types.is_numeric_dtype(df[col]):
            col_info['feature_type'] = 'numeric'

            # Compute scaling statistics for numeric columns
            col_info['mean'] = float(df[col].mean())
            col_info['std'] = float(df[col].std())
            col_info['min'] = float(df[col].min())
            col_info['max'] = float(df[col].max())
            col_info['median'] = float(df[col].median())

            # Additional useful statistics
            col_info['q25'] = float(df[col].quantile(0.25))
            col_info['q75'] = float(df[col].quantile(0.75))
            col_info['null_count'] = int(df[col].isnull().sum())

        else:
            col_info['feature_type'] = 'categorical'

            # For categorical columns, store unique values and counts
            col_info['unique_values'] = df[col].unique().tolist()
            col_info['num_unique'] = int(df[col].nunique())
            col_info['value_counts'] = df[col].value_counts().to_dict()
            col_info['null_count'] = int(df[col].isnull().sum())

        schema[col] = col_info

    # Add metadata about the dataset
    schema['_metadata'] = {
        'total_rows': int(len(df)),
        'total_columns': int(len(df.columns)),
        'numeric_columns': int(df.select_dtypes(include=[np.number]).shape[1]),
        'categorical_columns': int(df.select_dtypes(include=['object']).shape[1]),
        'creation_date': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
        'source_file': str(input_path)
    }

    # Save schema to JSON
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(schema, f, indent=2)

    print(f"\nSchema saved to: {output_path}")
    print(f"Total features documented: {len(schema) - 1}")  # -1 for metadata

    return schema


input_path = "../data/cleaned/wednesday_cleaned.csv"
output_path = "../data/final_features.json"

# Build the schema
schema = build_schema(input_path, output_path)
