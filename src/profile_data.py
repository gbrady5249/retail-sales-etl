import pandas as pd


file_path = "data/raw/Online Retail.xlsx"

df = pd.read_excel(file_path)

print("=== DATASET SHAPE ===")
print(df.shape)

print("\n=== COLUMNS ===")
print(df.columns.tolist())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATE ROWS ===")
print(df.duplicated().sum())

print("\n=== FIRST 5 ROWS ===")
print(df.head())