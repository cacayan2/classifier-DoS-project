print("All columns before formatting:")
print(df.columns.tolist())

# Clean column names: remove leading/trailing spaces and replace spaces with underscores
df.columns = df.columns.str.strip().str.replace(' ', '_')

print("All columns after formatting:")
print(df.columns.tolist())

# Find and drop all columns with constant values (including all zeros)
constant_columns = [col for col in df.columns if df[col].nunique() == 1]

print(f"Found {len(constant_columns)} constant columns:")
for col in constant_columns:
    print(f"  {col} = {df[col].iloc[0]}")

# Drop all constant columns
df = df.drop(columns=constant_columns)
print(f"\nShape: {df.shape}")

# Checking if these columns have duplicate data
print((df['Fwd_Header_Length'] == df['Fwd_Header_Length.1']).all())

df = df.drop(columns=['Fwd_Header_Length.1'])
print(f"Shape: {df.shape}")

# Identify columns with all NaN values
# Since there are no such columns, this will print an empty list
all_nan_columns = df.columns[df.isna().all()].tolist()

print(f"Columns with all NaN values: {all_nan_columns}")

# Drop rows with any NaN values
df = df.dropna(axis=0, how='any')

print(f"Shape: {df.shape}")

# Load data
df = pd.read_csv("../data/cleaned/wednesday_cleaned.csv")
print(f"Original shape: {df.shape}")

# Check infinite values in the two columns
columns_to_check = ['Flow_Bytes/s', 'Flow_Packets/s']

for col in columns_to_check:
    inf_count = np.isinf(df[col]).sum()
    print(f"{col}: {inf_count} infinite values")

# Remove rows with infinite values in these columns
df = df[np.isfinite(df['Flow_Bytes/s']) & np.isfinite(df['Flow_Packets/s'])]

print(f"New shape: {df.shape}")
print(f"Rows removed: {61006 - df.shape[0]}")

# Save the cleaned data
df.to_csv("../data/cleaned/wednesday_cleaned.csv", index=False)
