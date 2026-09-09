import pandas as pd


file_path = "data/raw/Online Retail.xlsx"

df = pd.read_excel(file_path)


print("=== UNIQUE VALUES ===")

print(f"Unique invoices: {df['InvoiceNo'].nunique():,}")
print(f"Unique products: {df['StockCode'].nunique():,}")
print(f"Unique customers: {df['CustomerID'].nunique():,}")
print(f"Unique countries: {df['Country'].nunique():,}")


print("\n=== DATE RANGE ===")

print(f"Start date: {df['InvoiceDate'].min()}")
print(f"End date:   {df['InvoiceDate'].max()}")


print("\n=== TOP 10 COUNTRIES BY TRANSACTION COUNT ===")

print(df["Country"].value_counts().head(10))


print("\n=== TOP 10 PRODUCTS BY QUANTITY SOLD ===")

positive_sales = df[df["Quantity"] > 0]

print(
    positive_sales.groupby("StockCode")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)