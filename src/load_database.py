import os

import psycopg
from dotenv import load_dotenv


CSV_FILE = "data/processed/online_retail_cleaned.csv"


def main():
    print("=== DATABASE LOAD ===")

    load_dotenv()

    connection = psycopg.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )

    print("✅ Connected to PostgreSQL")

    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE retail_transactions;")

        print("✅ Cleared existing rows")

        with open(CSV_FILE, "r", encoding="utf-8") as file:
            with cursor.copy(
                """
                COPY retail_transactions
                FROM STDIN
                WITH (FORMAT CSV, HEADER TRUE)
                """
            ) as copy:
                while data := file.read(1024 * 1024):
                    copy.write(data)

    connection.commit()
    connection.close()

    print("✅ Data loaded into PostgreSQL")


if __name__ == "__main__":
    main()