import pandas as pd


INPUT_FILE = "data/raw/Online Retail.xlsx"
OUTPUT_FILE = "data/processed/online_retail_cleaned.csv"


def main():
    print("=== RETAIL SALES ETL ===")
    print("Loading raw data...")

    df = pd.read_excel(INPUT_FILE)

    print(f"Raw rows: {len(df):,}")

    # Remove exact duplicate records
    df = df.drop_duplicates()

    print(f"Rows after removing duplicates: {len(df):,}")

    # Remove non-sales accounting adjustments
    df = df[df["Description"] != "Adjust bad debt"]

    print(f"Rows after removing accounting adjustments: {len(df):,}")

    # Create transaction classification
    df["TransactionType"] = "Sale"

    df.loc[
        df["Quantity"] < 0,
        "TransactionType"
    ] = "Return"

    # Calculate total transaction amount
    df["SalesAmount"] = df["Quantity"] * df["UnitPrice"]

    # Save processed data
    df.to_csv(OUTPUT_FILE, index=False)

    print("\n=== TRANSFORMATION COMPLETE ===")
    print(f"Processed rows: {len(df):,}")
    print(f"Sales transactions: {(df['TransactionType'] == 'Sale').sum():,}")
    print(f"Return transactions: {(df['TransactionType'] == 'Return').sum():,}")
    print(f"Output file: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()