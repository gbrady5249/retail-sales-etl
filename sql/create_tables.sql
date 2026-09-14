DROP TABLE IF EXISTS retail_transactions;

CREATE TABLE retail_transactions (
    invoice_no VARCHAR(20),
    stock_code VARCHAR(20),
    description TEXT,
    quantity INTEGER,
    invoice_date TIMESTAMP,
    unit_price NUMERIC(10, 2),
    customer_id NUMERIC(10, 0),
    country VARCHAR(100),
    transaction_type VARCHAR(10),
    sales_amount NUMERIC(12, 2)
);