-- views.sql — Reusable views for Power BI / reporting

CREATE OR REPLACE VIEW vw_monthly_sales AS
SELECT date_trunc('month', order_date)::date AS month, region, category,
       SUM(sales) AS sales, SUM(profit) AS profit, COUNT(DISTINCT order_id) AS orders
FROM fact_sales GROUP BY 1,2,3;

CREATE OR REPLACE VIEW vw_kpi_overview AS
SELECT 
  (SELECT SUM(sales) FROM fact_sales) AS total_sales,
  (SELECT SUM(profit) FROM fact_sales) AS total_profit,
  (SELECT SUM(profit)/NULLIF(SUM(sales),0) FROM fact_sales) AS margin_pct;

-- Use vw_monthly_sales as Power BI import view for trend visuals
