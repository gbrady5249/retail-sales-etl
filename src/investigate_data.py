import pandas as pd


file_path = "data/raw/Online Retail.xlsx"

df = pd.read_excel(file_path)

print("=== NEGATIVE QUANTITIES ===")
negative_quantity = df[df["Quantity"] < 0]

print(f"Rows with negative quantity: {len(negative_quantity)}")
print(negative_quantity.head(10))


print("\n=== ZERO QUANTITIES ===")
zero_quantity = df[df["Quantity"] == 0]

print(f"Rows with zero quantity: {len(zero_quantity)}")


print("\n=== INVOICE NUMBERS STARTING WITH C ===")
cancelled = df[df["InvoiceNo"].astype(str).str.startswith("C")]

print(f"Potential cancellations: {len(cancelled)}")
print(cancelled.head(10))


print("\n=== NEGATIVE UNIT PRICES ===")
negative_price = df[df["UnitPrice"] < 0]

print(f"Rows with negative price: {len(negative_price)}")
print(negative_price.head(10))