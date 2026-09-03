# Business Requirements — Sales & Profit Analytics

## Stakeholder
Sales & Finance leadership. Needs a single view to track Sales, Profit, Margin and decide where to invest/discount next quarter.

## KPIs
- **Total Sales** (SUM Sales)
- **Total Profit** (SUM Profit)
- **Margin %** = Profit / Sales
- **Orders, Customers, AOV**
- **YoY Sales/Profit %**, **YTD**

## Dimensions for slicing
Date (Year/Quarter/Month), Region, State, City, Category, Sub-Category, Segment, Ship Mode

## Questions the dashboard must answer
1. Are we growing profitably? (Sales vs Profit trend, Margin % over time)
2. Which region/category/segment is most profitable vs largest revenue?
3. Where is discount eroding margin?
4. Who are top/bottom 10 products and customers by profit?

## Acceptance criteria
- One Overview page with 4 KPI cards + trend + region/category breakdown
- Profitability page with margin % and discount analysis
- Details table with search/sort, responsive slicers
- DAX measures documented, model is star schema
