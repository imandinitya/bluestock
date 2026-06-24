import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        print("\n" + "="*60)
        print(f"Dataset: {file}")

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())
    
    
print("\n" + "="*60)
print("FUND MASTER EXPLORATION")
print("="*60)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

print("\nColumns:")
print(fund_master.columns)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv"
)   

print(fund_master.columns)
print(nav_history.columns)

master_codes = set(
    fund_master['amfi_code']
)

nav_codes = set(
    nav_history['amfi_code']
)

missing_codes = master_codes - nav_codes

print(
    f"Missing codes: {len(missing_codes)}"
)