# DAX Measures

```DAX
Total Sales = SUM(FactSales[Sales])
Total Profit = SUM(FactSales[Profit])
Total Quantity = SUM(FactSales[Quantity])
Orders = DISTINCTCOUNT(FactSales[Order ID])

Margin % = DIVIDE([Total Profit], [Total Sales])

AOV = DIVIDE([Total Sales], [Orders])

Sales YTD = TOTALYTD([Total Sales], DimDate[Date])
Profit YTD = TOTALYTD([Total Profit], DimDate[Date])

Sales YoY % = 
VAR Prev = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(DimDate[Date]))
RETURN DIVIDE([Total Sales] - Prev, Prev)

Profit YoY % = 
VAR Prev = CALCULATE([Total Profit], SAMEPERIODLASTYEAR(DimDate[Date]))
RETURN DIVIDE([Total Profit] - Prev, Prev)

Top Product Profit = CALCULATE([Total Profit], TOPN(1, DimProduct, [Total Profit]))
```

**Formatting:** Sales/Profit as currency, Margin/YoY as %, 1 decimal. Use DIVIDE to avoid /0.
