# Retail Sales ETL Pipeline

## Overview

An end-to-end data engineering project that transforms raw retail transaction data into a validated, analytics-ready PostgreSQL database.

The pipeline uses Python and pandas to clean and transform more than 500,000 retail transactions, performs automated data quality checks, creates the required PostgreSQL schema, and loads the processed data into the database.

The entire ETL workflow can be executed through a single Python command, making the pipeline reproducible and easy to rerun.

## Project Goals

- Build a reproducible end-to-end ETL pipeline
- Clean and transform raw transactional data using Python and pandas
- Implement automated data quality validation
- Load processed data into PostgreSQL
- Automate PostgreSQL schema creation and data loading
- Write SQL queries to analyze revenue, returns, customers, products, and geographic performance
- Apply Git and GitHub version control throughout development

## Architecture

The pipeline follows a sequential ETL workflow:

Raw Excel Dataset  
↓  
Python / pandas Transformation  
↓  
Data Quality Validation  
↓  
PostgreSQL Schema Setup  
↓  
PostgreSQL Data Load  
↓  
SQL Analytics

The pipeline is orchestrated by `src/run_pipeline.py`, which executes each stage in order and stops if a step fails.

## Repository Structure

```text
retail-sales-etl/
├── data/
│   ├── raw/                     # Raw source data (excluded from Git)
│   └── processed/               # Generated cleaned data (excluded from Git)
├── sql/
│   ├── analysis_queries.sql     # SQL queries for business analysis
│   └── create_tables.sql        # PostgreSQL table schema
├── src/
│   ├── investigate_data.py      # Source data investigation
│   ├── load_database.py         # PostgreSQL bulk loading
│   ├── profile_data.py          # Initial data profiling
│   ├── run_pipeline.py          # End-to-end pipeline orchestrator
│   ├── setup_database.py        # PostgreSQL schema setup
│   ├── transform_data.py        # Data cleaning and transformation
│   └── validate_data.py         # Automated data quality checks
├── .env.example                 # Environment variable template
├── .gitignore                   # Files excluded from version control
├── data_dictionary.md           # Dataset field definitions
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

## Technologies

- **Python** — pipeline orchestration and ETL logic
- **pandas** — data cleaning, transformation, and validation
- **PostgreSQL** — relational database and analytical storage
- **SQL** — schema creation and business analysis queries
- **psycopg** — Python-to-PostgreSQL connectivity and bulk loading
- **openpyxl** — Excel source-file support
- **python-dotenv** — environment-based database credential management
- **Git & GitHub** — version control and project hosting

## Data Source

This project uses the **Online Retail** dataset from the UCI Machine Learning Repository.

The dataset contains transactional data from a UK-based online retailer and includes:

- **541,909 raw transaction records**
- **25,900 unique invoices**
- **4,070 unique products**
- **4,372 unique customers**
- **38 countries**
- Transaction dates from **December 2010 through December 2011**

The raw dataset is stored locally in `data/raw/` and is excluded from GitHub through `.gitignore`.

Initial data profiling identified duplicate records, missing customer IDs and product descriptions, product returns, cancelled invoices, and accounting adjustment records. These findings informed the transformation and validation rules used by the ETL pipeline.

## Data Transformation

The transformation stage converts the raw retail dataset into a cleaned, analytics-ready dataset.

Key transformation rules include:

- Remove exact duplicate transaction records
- Remove non-sales accounting adjustments such as `Adjust bad debt`
- Classify transactions with negative quantities as `Return`
- Classify remaining transactions as `Sale`
- Create a `SalesAmount` field calculated as `Quantity × UnitPrice`
- Preserve valid returns so they can be included in net-revenue analysis

After transformation, the dataset is reduced from **541,909 raw rows to 536,638 processed rows**, consisting of:

- **526,051 sales transactions**
- **10,587 return transactions**

## Data Quality Validation

Before data is loaded into PostgreSQL, the pipeline automatically validates the processed dataset.

Validation checks include:

- No exact duplicate records
- All required columns are present
- Required transaction fields contain no missing values
- Unit prices are not negative
- `SalesAmount` equals `Quantity × UnitPrice`
- `TransactionType` contains only valid `Sale` or `Return` values

If any validation check fails, the pipeline raises an error and stops before the data is loaded into PostgreSQL. This prevents invalid data from reaching the analytical database.

## SQL Analysis & Key Findings

After loading the validated dataset into PostgreSQL, SQL queries are used to analyze sales performance, returns, customers, products, countries, and monthly revenue trends.

Key findings include:

- **Gross sales revenue:** $10,631,048.74
- **Return value:** $893,979.73
- **Net revenue:** $9,737,069.01
- **Unique customers:** 4,372
- **Highest-revenue country:** United Kingdom
- **Highest full-month net revenue:** November 2011 at approximately $1.46 million

The analysis also identified shipping and service charges such as `DOTCOM POSTAGE` and `POSTAGE` among the highest-revenue descriptions. These records were retained rather than automatically classified as products because excluding them would require an explicit business rule.

Analytical queries are available in `sql/analysis_queries.sql`.

## Running the Pipeline

### Prerequisites

Before running the pipeline, ensure that Python and PostgreSQL are installed and that a PostgreSQL database named `retail_sales` has been created.

### 1. Install dependencies

```powershell
pip install -r requirements.txt
```

### 2. Configure PostgreSQL credentials

Create a `.env` file in the project root:

```text
POSTGRES_PASSWORD=your_postgresql_password
```

The `.env` file is excluded from Git through `.gitignore` so database credentials are not committed to the repository.

### 3. Add the source dataset

Place the UCI Online Retail Excel file at:

```text
data/raw/Online Retail.xlsx
```

### 4. Run the pipeline

```powershell
python src/run_pipeline.py
```

The command automatically:

1. Transforms the raw dataset
2. Validates data quality
3. Creates the PostgreSQL table
4. Loads the validated data into PostgreSQL

A successful run loads **536,638 validated transaction records** into the `retail_transactions` table.

## Project Status

Core ETL functionality is complete.

Completed components include:

- Data profiling and source investigation
- Python-based transformation
- Automated data quality validation
- PostgreSQL schema creation
- Automated PostgreSQL loading
- SQL business analysis
- End-to-end pipeline orchestration

Current work is focused on documentation, repository polish, and portfolio presentation.