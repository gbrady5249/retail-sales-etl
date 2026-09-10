import pandas as pd


INPUT_FILE = "data/processed/online_retail_cleaned.csv"


def main():
    print("=== DATA VALIDATION ===")

    df = pd.read_csv(INPUT_FILE)

    print(f"Rows being validated: {len(df):,}")

    errors = []

    # Check for duplicate rows
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        errors.append(f"Found {duplicate_count:,} duplicate rows")
    else:
        print("✓ No duplicate rows")

    # Required columns
    required_columns = [
        "InvoiceNo",
        "StockCode",
        "Quantity",
        "UnitPrice",
        "SalesAmount",
        "TransactionType",
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        errors.append(f"Missing columns: {missing_columns}")
    else:
        print("✓ All required columns present")

    # Check required fields for missing values
    for column in ["InvoiceNo", "StockCode", "Quantity", "UnitPrice"]:
        missing_count = df[column].isna().sum()

        if missing_count > 0:
            errors.append(
                f"{column} contains {missing_count:,} missing values"
            )
        else:
            print(f"✓ {column} has no missing values")

    # Unit price should not be negative
    negative_prices = (df["UnitPrice"] < 0).sum()

    if negative_prices > 0:
        errors.append(
            f"Found {negative_prices:,} rows with negative UnitPrice"
        )
    else:
        print("✓ No negative unit prices")

    # Validate SalesAmount calculation
    expected_sales_amount = df["Quantity"] * df["UnitPrice"]

    calculation_errors = (
        (df["SalesAmount"] - expected_sales_amount).abs() > 0.01
    ).sum()

    if calculation_errors > 0:
        errors.append(
            f"Found {calculation_errors:,} incorrect SalesAmount values"
        )
    else:
        print("✓ SalesAmount calculations are correct")

    # Validate transaction types
    valid_transaction_types = {"Sale", "Return"}

    invalid_types = set(df["TransactionType"].dropna().unique()) - valid_transaction_types

    if invalid_types:
        errors.append(
            f"Invalid TransactionType values: {invalid_types}"
        )
    else:
        print("✓ TransactionType values are valid")

    # Final result
    print("\n=== VALIDATION RESULT ===")

    if errors:
        print("❌ VALIDATION FAILED")

        for error in errors:
            print(f"- {error}")

        raise ValueError("Data validation failed")

    print("✅ VALIDATION PASSED")


if __name__ == "__main__":
    main()