-- 03_advanced_analysis.sql — Window functions, Top N, profitability

-- Top 10 products by profit (and bottom 10)
SELECT product_name, SUM(sales) AS sales, SUM(profit) AS profit
FROM fact_sales GROUP BY product_name ORDER BY profit DESC LIMIT 10;

SELECT product_name, SUM(profit) AS profit
FROM fact_sales GROUP BY product_name ORDER BY profit ASC LIMIT 10;

-- Top 10 customers by profit
SELECT customer_id, customer_name, SUM(profit) AS profit, SUM(sales) AS sales
FROM fact_sales GROUP BY customer_id, customer_name ORDER BY profit DESC LIMIT 10;

-- YoY by month (window)
WITH monthly AS (
  SELECT date_trunc('month', order_date) AS m, SUM(sales) AS sales
  FROM fact_sales GROUP BY 1
)
SELECT m, sales,
  LAG(sales,12) OVER (ORDER BY m) AS sales_same_month_last_year,
  (sales - LAG(sales,12) OVER (ORDER BY m)) / NULLIF(LAG(sales,12) OVER (ORDER BY m),0) AS yoy_pct
FROM monthly ORDER BY m;

-- Region profitability rank per year
SELECT 
  EXTRACT(YEAR FROM order_date) AS yr, region, SUM(profit) AS profit,
  RANK() OVER (PARTITION BY EXTRACT(YEAR FROM order_date) ORDER BY SUM(profit) DESC) AS rnk
FROM fact_sales GROUP BY yr, region ORDER BY yr, rnk;

-- Segment AOV vs Discount
SELECT segment, 
  SUM(sales)/NULLIF(COUNT(DISTINCT order_id),0) AS aov,
  AVG(discount) AS avg_discount,
  SUM(profit)/NULLIF(SUM(sales),0) AS margin_pct
FROM fact_sales GROUP BY segment;
