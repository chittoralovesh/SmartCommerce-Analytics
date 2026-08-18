# Power BI Dashboard Structure

## Global Elements (Across all pages)
- **Navigation Bar:** Left-side menu with icons for switching between pages.
- **Filter Pane (Slicers):** Date Range (Year/Quarter/Month), Region, Category, Segment.
- **Color Theme:** Modern dark theme (Navy/Charcoal background) with neon/bright accents (Teal, Orange, Lime Green) or a clean corporate light theme (White/Grey with Blue/Green data bars).

---

## 1. Executive Summary
**Goal:** High-level overview for C-suite.
- **KPI Cards:** Total Revenue, Total Profit, Profit Margin %, Total Orders, YoY Growth.
- **Charts:**
  - Area Chart: Monthly Sales vs. Profit trend.
  - Donut Chart: Sales by Category.
  - Map Visual: Sales by State/Region (bubble size = Sales, color saturation = Profit Margin).
- **Interactivity:** Drill-through on Map to see Regional Analysis.

## 2. Sales Performance
**Goal:** Deep dive into revenue generation.
- **KPI Cards:** Average Order Value, Total Units Sold, Sales per Customer.
- **Charts:**
  - Bar Chart: Sales by Sub-Category.
  - Waterfall Chart: Month-over-Month Sales Variance.
  - Matrix Table: Year/Quarter/Month hierarchy showing Sales, Target, and Variance.

## 3. Customer Insights
**Goal:** Understand buying behavior and segments.
- **KPI Cards:** Total Active Customers, New vs. Returning Customers, Customer Lifetime Value (CLV).
- **Charts:**
  - Scatter Plot: Sales vs. Discount by Segment.
  - Tree Map: Customer Segments breakdown.
  - Table: Top 10 Customers with drill-through to individual transaction history.

## 4. Product Analytics
**Goal:** Evaluate product portfolio profitability.
- **KPI Cards:** Most Profitable Product, Highest Selling Product (Units).
- **Charts:**
  - Column Chart: Profit Margin by Product Sub-Category.
  - Scatter Plot (Quadrant Analysis): Profit vs. Sales (Identify Cash Cows vs. Dogs).
  - Ribbon Chart: Top 5 Sub-Categories Rank changes over quarters.

## 5. Regional Analysis
**Goal:** Assess geographical performance.
- **KPI Cards:** Best Performing Region, Worst Performing Region.
- **Charts:**
  - Filled Map: State-by-State profit distribution.
  - Clustered Bar Chart: Sales & Profit by City (Top 10).
  - Gauge Chart: Regional Sales vs. Regional Targets.

## 6. Forecasting & Trends
**Goal:** Predictive analytics using Power BI built-in features.
- **Charts:**
  - Line Chart with Forecast Analytics line (Predicting next 6 months of sales).
  - Key Influencers Visual: What drives Profit to increase/decrease?
  - Q&A Visual: Natural language querying for users (e.g., "Show sales in California for 2023").
