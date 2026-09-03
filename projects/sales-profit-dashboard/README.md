# Sales & Profit Analytics Dashboard — Power BI • SQL

> **Flagship BI case study.** End-to-end: Business questions → SQL modeling → Power Query → DAX star schema → Power BI dashboard → Insights & recommendations.

**Live Case Study:** `https://rizz1406.github.io/projects/sales-profit-dashboard/`  
**Stack:** Power BI, DAX, Power Query (M), SQL (Window functions, CTEs), Excel, Git

### Business Questions Answered
1. What are total Sales, Profit, Margin % and how are they trending YoY?
2. Which regions / categories / segments drive profit, and where does margin leak?
3. Which products/customers are most/least profitable?
4. Where should we act next quarter to protect margin?

### Dashboard Highlights
- **Star schema** (Fact Sales + Dim Date/Product/Customer/Region)
- **12 DAX measures** (Total Sales, Total Profit, Margin %, YTD, YoY %)
- **Pages:** Overview (KPIs) → Sales Deep-Dive → Profit & Margin → Details
- **Interactivity:** Slicers for Date/Region/Category, cross-filtering, drill-through

### Repository Structure
```
projects/sales-profit-dashboard/
├── docs/           # Requirements, dictionary, model, DAX, insights
├── data/raw/       # Original CSV (sample)
├── data/processed/ # Cleaned CSV
├── sql/            # Schema + KPI + advanced queries
├── powerbi/        # .pbix, M code, theme.json
├── screenshots/    # Dashboard exports
└── exports/        # PDF one-pagers
```

### How to Run
1. Open `powerbi/sales-profit-dashboard.pbix` in Power BI Desktop
2. Or run SQL in `sql/` against `data/processed/sales_cleaned.csv` (import to Postgres/MySQL/SQLite)
3. Screenshots in `screenshots/` are standalone if Power BI not installed

### Key Insights (preview)
- West region leads profit but Central drags margin by -4.2 pts
- Technology category has highest margin; Furniture leaks profit on discounts >20%
- Top 10 customers = 18% of profit — retention risk

See `docs/insights-and-recommendations.md` for full writeup.

### Author
Rizwan Baig — Data Analyst | [Portfolio](https://rizz1406.github.io) • [LinkedIn](https://www.linkedin.com/in/rizwanbaig001/) • [GitHub](https://github.com/rizz1406)
