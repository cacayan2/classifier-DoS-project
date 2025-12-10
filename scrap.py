import pandas as pd
import sys
from pathlib import Path
import pyperclip


project_root = Path(".").resolve()
sys.path.insert(0, str(project_root))

data_path = project_root / "data" / "cleaned" / "wednesday_cleaned.csv"
df = pd.read_csv(data_path)
print(df.head(20))