-- 02_kpi_queries.sql — Core KPIs for dashboard

-- Overall KPIs
SELECT 
  SUM(sales) AS total_sales,
  SUM(profit) AS total_profit,
  SUM(profit)/NULLIF(SUM(sales),0) AS margin_pct,
  COUNT(DISTINCT order_id) AS orders,
  SUM(sales)/NULLIF(COUNT(DISTINCT order_id),0) AS aov
FROM fact_sales;

-- Sales & Profit by Region
SELECT region, SUM(sales) AS sales, SUM(profit) AS profit, SUM(profit)/NULLIF(SUM(sales),0) AS margin_pct
FROM fact_sales GROUP BY region ORDER BY profit DESC;

-- By Category / Sub-Category
SELECT category, sub_category, SUM(sales) AS sales, SUM(profit) AS profit, AVG(discount) AS avg_discount
FROM fact_sales GROUP BY category, sub_category ORDER BY profit DESC;

-- Monthly trend (for YoY)
SELECT date_trunc('month', order_date) AS month, SUM(sales) AS sales, SUM(profit) AS profit
FROM fact_sales GROUP BY 1 ORDER BY 1;

-- Discount vs Profit leak
SELECT 
  CASE 
    WHEN discount = 0 THEN '0%'
    WHEN discount <= 0.2 THEN '1-20%'
    WHEN discount <= 0.4 THEN '21-40%'
    ELSE '>40%'
  END AS discount_bucket,
  COUNT(*) AS orders, SUM(sales) AS sales, SUM(profit) AS profit
FROM fact_sales GROUP BY 1 ORDER BY 1;
