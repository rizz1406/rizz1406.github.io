-- 01_schema_and_cleaning.sql
-- Postgres / SQLite compatible. Load data/processed/sales_cleaned.csv into fact_sales

DROP TABLE IF EXISTS fact_sales;
CREATE TABLE fact_sales (
  order_id TEXT,
  order_date DATE,
  ship_date DATE,
  ship_mode TEXT,
  customer_id TEXT,
  customer_name TEXT,
  segment TEXT,
  country TEXT,
  region TEXT,
  state TEXT,
  city TEXT,
  category TEXT,
  sub_category TEXT,
  product_name TEXT,
  sales NUMERIC,
  quantity INT,
  discount NUMERIC,
  profit NUMERIC
);

-- Example cleaning checks after import
-- 1. Trim + type checks
SELECT COUNT(*) AS bad_dates FROM fact_sales WHERE order_date > ship_date;
SELECT COUNT(*) AS bad_sales FROM fact_sales WHERE sales <= 0;
SELECT COUNT(*) AS bad_discount FROM fact_sales WHERE discount < 0 OR discount > 0.8;

-- 2. De-duplicate (keep one per order_id + product_name)
-- SELECT order_id, product_name, COUNT(*) FROM fact_sales GROUP BY 1,2 HAVING COUNT(*)>1;

-- 3. Null audit
SELECT 
  SUM((customer_id IS NULL)::int) AS null_customer,
  SUM((sales IS NULL)::int) AS null_sales
FROM fact_sales;
