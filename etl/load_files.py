import pandas as pd
import json
import pyarrow.parquet as pq
from pathlib import Path


def read_all_files(folder_path):
    """
    Read all CSV, JSON, and Parquet files from a folder and combine into a single DataFrame.

    Args:
        folder_path: Path to the folder containing the data files

    Returns:
        Combined pandas DataFrame
    """
    folder = Path(folder_path)
    dataframes = []

    # Read all CSV files
    for csv_file in folder.glob("*.csv"):
        print(f"Reading CSV: {csv_file.name}")
        df = pd.read_csv(csv_file)
        dataframes.append(df)

    # Read all JSON files
    for json_file in folder.glob("*.json"):
        print(f"Reading JSON: {json_file.name}")
        try:
            # Try JSON Lines format first (most common for data files)
            tmp_df = pd.read_json(json_file, lines=True)
            dataframes.append(tmp_df)
        except ValueError:
            print(f"Warning: Unexpected JSON structure in {json_file.name}")
        # tmp_df = pd.read_json(json_file, lines=True)
        # dataframes.append(tmp_df)

    # Read all Parquet files
    for parquet_file in folder.glob("*.parquet"):
        print(f"Reading Parquet: {parquet_file.name}")
        table = pq.read_table(parquet_file)
        df = table.to_pandas()
        dataframes.append(df)

    # Combine all dataframes
    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        return combined_df
    else:
        print("No files found!")
        return pd.DataFrame()


# Usage
folder_path = "fall2025_L/"  # Change the folder path here for your data directory
df = read_all_files(folder_path)
print(f"Combined DataFrame shape: {df.shape}")

# Check if 'labels' column exists
if ' Label' in df.columns:
    print("\nUnique values in 'label' column:")
    print(df[' Label'].unique())

    print("\nValue counts:")
    print(df[' Label'].value_counts())

    print(f"\nTotal unique labels: {df[' Label'].nunique()}")
else:
    print("'labels' column not found in the dataframe")
    print(f"Available columns: {df.columns.tolist()}")

# Remove all rows with 'Heartbleed' label
df = df[df[' Label'] != 'Heartbleed']

# Create binary column: 0 for BENIGN, 1 for all attacks
df['Attack'] = (df[' Label'] != 'BENIGN').astype(int)

# Verify the changes
print("\nAfter removing Heartbleed:")
print(df[' Label'].value_counts())

print("\nBinary label distribution:")
print(df['Attack'].value_counts())

# Save the combined dataframe to CSV
output_path = "data/interm/combined_raw.csv"

# Create the directory if it doesn't exist
Path(output_path).parent.mkdir(parents=True, exist_ok=True)

# Save to CSV
print(f"\nSaving dataframe to {output_path}...")
df.to_csv(output_path, index=False)
print(
    f"Successfully saved! File size: {Path(output_path).stat().st_size / (1024*1024):.2f} MB")
