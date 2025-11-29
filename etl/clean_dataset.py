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
