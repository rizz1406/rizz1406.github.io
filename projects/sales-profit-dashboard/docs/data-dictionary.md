# Data Dictionary

Source: Superstore-style sales dataset (synthetic, retail orders 2019-2023)

| Column | Type | Description |
|---|---|---|
| Order ID | TEXT | Unique order identifier |
| Order Date | DATE | Order placed date |
| Ship Date | DATE | Shipped date |
| Ship Mode | TEXT | Standard / Second Class / First Class / Same Day |
| Customer ID | TEXT | FK to Customer |
| Customer Name | TEXT | Display name |
| Segment | TEXT | Consumer / Corporate / Home Office |
| Country/Region/State/City | TEXT | Geography |
| Category | TEXT | Furniture / Office Supplies / Technology |
| Sub-Category | TEXT | Chairs, Phones, etc. |
| Product Name | TEXT | SKU name |
| Sales | NUMERIC | Line sales (qty * price) |
| Quantity | INT | Units |
| Discount | NUMERIC | 0-0.8 |
| Profit | NUMERIC | Sales - Cost - Discount impact |

## Quality rules
- Sales > 0, Quantity 1-14, Discount 0-0.8, Profit can be negative
- Order Date <= Ship Date
- No duplicate Order ID + Product Name

## Lineage
raw/sales_superstore_raw.csv → Power Query (type casting, trim, date parse) → processed/sales_cleaned.csv → SQL views → Power BI model
