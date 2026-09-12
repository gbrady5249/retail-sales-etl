-- Transaction counts by type
SELECT
    transaction_type,
    COUNT(*) AS transaction_count
FROM retail_transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;

-- Total sales revenue
SELECT
    ROUND(SUM(sales_amount), 2) AS total_sales_revenue
FROM retail_transactions
WHERE transaction_type = 'Sale';

-- Total return value
SELECT
    ROUND(ABS(SUM(sales_amount)), 2) AS total_return_value
FROM retail_transactions
WHERE transaction_type = 'Return';

-- Net revenue after returns
SELECT
    ROUND(SUM(sales_amount), 2) AS net_revenue
FROM retail_transactions;

-- Unique customers
SELECT
    COUNT(DISTINCT customer_id) AS unique_customers
FROM retail_transactions;

-- Top 10 countries by net revenue
SELECT
    country,
    ROUND(SUM(sales_amount), 2) AS net_revenue
FROM retail_transactions
GROUP BY country
ORDER BY net_revenue DESC
LIMIT 10;

-- Top 10 products by net revenue
SELECT
    description,
    ROUND(SUM(sales_amount), 2) AS net_revenue
FROM retail_transactions
WHERE description IS NOT NULL
GROUP BY description
ORDER BY net_revenue DESC
LIMIT 10;

-- Monthly net revenue
SELECT
    DATE_TRUNC('month', invoice_date) AS month,
    ROUND(SUM(sales_amount), 2) AS net_revenue
FROM retail_transactions
GROUP BY DATE_TRUNC('month', invoice_date)
ORDER BY month;