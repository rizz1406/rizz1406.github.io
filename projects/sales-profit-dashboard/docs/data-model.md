# Data Model — Star Schema

## Diagram (text)
```
DimDate (Date PK) ─┐
DimProduct (Product PK) ─┤
DimCustomer (Customer PK) ─┼─ FactSales (OrderID + ProductID composite)
DimGeography (Region/State/City) ─┤
DimShipMode ─┘
```

## FactSales grain
One row per OrderID + Product. Measures: Sales, Quantity, Discount, Profit (additive).

## Relationships
- FactSales[OrderDate] → DimDate[Date] (many:1)
- FactSales[Product Name] → DimProduct[Product] (many:1, or surrogate ProductID)
- FactSales[Customer ID] → DimCustomer[CustomerID] (many:1)
- All dimensions single direction, no bi-directional filtering.

## Why star vs flat
Faster DAX, clean slicers, proper YTD/YoY via DimDate, single source for geography.

## Calendar table (DAX)
```DAX
DimDate = CALENDAR(DATE(2019,1,1), DATE(2023,12,31))
Year = YEAR([Date])
Month = FORMAT([Date],"MMM")
Quarter = "Q" & FORMAT([Date],"Q")
```
