import os

import psycopg
from dotenv import load_dotenv


SQL_FILE = "sql/create_tables.sql"


def main():
    print("=== DATABASE SETUP ===")

    load_dotenv()

    connection = psycopg.connect(
        dbname="retail_sales",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD"),
        host="localhost",
        port="5432",
    )

    print(" ✔️  Connected to PostgreSQL")

    with open(SQL_FILE, "r", encoding="utf-8") as file:
        sql = file.read()

    with connection.cursor() as cursor:
        cursor.execute(sql)

    connection.commit()
    connection.close()

    print(" ✔️  Database table created")


if __name__ == "__main__":
    main()