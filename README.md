# retail-sales-analytics
End-to-end retail analytics pipeline: exploratory analysis in Python, business queries in SQL, A/B testing and time-series forecasting in R, and an interactive Tableau dashboard. Analyzes 15,000+ multi-channel transactions across product categories, customer segments, and promotional strategies.
[README.md](https://github.com/user-attachments/files/26447653/README.md)
# Multi-Channel Retail Sales Analytics

An end-to-end data analytics project analyzing 15,000+ retail transactions across multiple sales channels, product categories, and customer segments. Built using Python, SQL, R, and Tableau to demonstrate a full analytics workflow — from data cleaning through statistical testing to interactive dashboard delivery.

**[View the Interactive Tableau Dashboard](https://public.tableau.com/app/profile/austin.sanders3768/viz/RetailAnalysisMiniProject/Dashboard1?publish=yes)**

---

## Business Context

A fictional multi-channel retail company sells products across five categories (Apparel, Toys, Home, Accessories, Collectibles) through four sales channels (Online Store, Theme Park Shop, Retail Partner, Pop-Up Event) in five regions. The dataset spans January 2024 through December 2025 and includes transaction-level detail on pricing, discounts, customer satisfaction, and returns.

The goal of this project is to answer the kinds of questions a retail analytics team faces daily:

- Where is revenue concentrated across channels and categories?
- How does seasonality affect demand, and can we forecast future revenue?
- Do promotional discounts increase return rates?
- Does customer spending behavior differ between weekends and weekdays?

---

## Project Structure

```
retail-sales-analytics/
│
├── README.md
├── theme_park_retail_sales.csv        # Dataset (~15,000 rows)
├── exploratory_analysis.py            # Python — EDA and data cleaning
├── business_queries.sqbpro              # SQL — KPI queries and channel analysis
├── retail_project.R         # R — ARIMA/ETS forecasting and A/B tests
|──Retail Analysis Mini Project.twb    #Interactive Tableau Dashboard
└── figures/                           # Saved charts and plots
    ├── monthly_revenue.png
    ├── revenue_by_category.png
    ├── correlation_heatmap.png
    ├── channel_mix_over_time.png
    ├── Decomp_TimeSeries.png.png
    └── 6-monthforecastv1.png.png
```

---

## Tools & Methods

| Tool    | Purpose                                                    |
|---------|------------------------------------------------------------|
| Python  | Data cleaning, EDA, visualization (pandas, matplotlib, seaborn) |
| SQL     | Business queries, KPI calculation (SQLite via DB Browser)  |
| R       | Time-series forecasting, A/B testing (tidyverse, forecast) |
| Tableau | Interactive dashboard with cross-filtered views            |

---

## Key Analyses

### Exploratory Data Analysis (Python)

- Validated data integrity: confirmed no missing values across 17 columns and 15,000+ rows
- Identified seasonal revenue peaks in summer (June–July) and the holiday season (November–December)
- Built a correlation heatmap to distinguish mechanically derived relationships from behaviorally meaningful ones
- Visualized revenue distribution across categories and channel mix over time

### Business Queries (SQL)

- Calculated eCommerce KPIs by sales channel: average order value, return rate, customer satisfaction, and promotion penetration rate
- Identified top 5 revenue-generating products and compared franchise-level return rates
- Analyzed weekend vs. weekday performance using CASE logic

### A/B Testing (R)

**Test 1 — Weekend vs. Weekday Spending:**
Welch's t-test comparing average order value between weekend and weekday customers. Result: no significant difference (p = 0.97, df = 9,480). Weekend revenue gains come from higher transaction volume, not higher per-order spending.

**Test 2 — Discount Impact on Returns:**
Welch's t-test comparing return rates between discounted and full-price orders. Result: no significant difference (p = 0.50, df = 11,725). Return rate was approximately 8% regardless of discount status, indicating promotions can be deployed without increasing reverse logistics costs.

### Time-Series Forecasting (R)

- Decomposed monthly revenue into trend, seasonal, and residual components
- Initial auto.arima selected ARIMA(0,0,1), which failed to capture seasonality — diagnosed via residual pattern analysis
- Iterated to seasonal ARIMA and ETS (AAA) models, producing forecasts that reflect the seasonal demand cycle
- Generated 6-month forecasts with 80% and 95% confidence intervals

---

## Dashboard Preview

The Tableau dashboard includes four interactive views:

1. **Monthly Revenue Trend** — line chart tracking net revenue over 24 months
2. **Revenue by Category** — horizontal bar chart ranking product categories
3. **Sales Channel Breakdown** — pie chart showing channel contribution
4. **Region × Category Heatmap** — cross-tabulated revenue intensity

All views are cross-filtered so selecting a category, date range, or channel updates the entire dashboard.

**[Open the live dashboard on Tableau Public](https://public.tableau.com/app/profile/austin.sanders3768/viz/RetailAnalysisMiniProject/Dashboard1?publish=yes)**

---

## Dataset Description

| Column                 | Type    | Description                              |
|------------------------|---------|------------------------------------------|
| order_id               | Integer | Unique transaction identifier            |
| order_date             | Date    | Transaction date (YYYY-MM-DD)            |
| month                  | Integer | Month number (1–12)                      |
| day_of_week            | Text    | Monday through Sunday                    |
| category               | Text    | Product category                         |
| product                | Text    | Specific product name                    |
| franchise              | Text    | IP franchise                             |
| sales_channel          | Text    | Online Store, Theme Park Shop, etc.      |
| region                 | Text    | Geographic region                        |
| unit_price             | Decimal | Price per unit (USD)                     |
| quantity               | Integer | Units purchased (1–5)                    |
| gross_revenue          | Decimal | unit_price × quantity                    |
| discount_pct           | Integer | Discount percentage (0–25%)              |
| discount_amt           | Decimal | Dollar discount amount                   |
| net_revenue            | Decimal | Revenue after discount                   |
| customer_satisfaction  | Integer | Rating (1–5 scale)                       |
| returned               | Integer | 0 = kept, 1 = returned                  |

---

## How to Reproduce

**Python:**
```bash
pip install pandas matplotlib seaborn
python exploratory_analysis.py
```

**SQL:**
Import `theme_park_retail_sales.csv` into DB Browser for SQLite, then run the queries in `business_queries.sql`.

**R:**
```r
install.packages(c("tidyverse", "forecast", "tseries", "lubridate"))
source("forecasting_and_ab_tests.R")
```

---

## Author

**Austin Sanders**
M.S. Applied Mathematics — University of Arkansas at Little Rock (Expected May 2026)
