# AI-Powered E-Commerce Analytics Dashboard

![Power BI Dashboard](dashboard.png)

## 📌 Project Overview
An end-to-end Business Intelligence and Data Analytics project designed to provide actionable insights for an e-commerce enterprise. This project integrates Data Cleaning (Python), Advanced Data Modeling (SQL), Interactive Visualization (Power BI), and Predictive Analytics concepts (Machine Learning) to solve real-world revenue and operational challenges.

## 🛠️ Tech Stack
- **Python (Pandas, Numpy, Seaborn):** Exploratory Data Analysis, Data Cleaning, and Feature Engineering.
- **SQL (PostgreSQL):** Complex querying, Window Functions, CTEs, and Aggregations for business logic.
- **Power BI & DAX:** Interactive dashboard design, relational data modeling, and KPI tracking.
- **Excel:** Initial data assessment and metadata documentation.

## 📊 Key Features & Dashboards
1. **Executive Summary:** High-level metrics for C-level executives (Revenue, Profit Margin, YoY Growth).
2. **Sales & Product Analytics:** Quadrant analysis of Profit vs. Sales to identify "Cash Cows" and "Loss Leaders".
3. **Customer Insights:** RFM Analysis (Recency, Frequency, Monetary) to segment customers.
4. **Predictive Forecasting:** AI-driven sales forecasting and discount impact simulation.

## 💡 Top Business Insights
- **Discount Cannibalization:** Discounts exceeding 20% correlate with a 45% drop in net profit margin.
- **Customer Pareto:** 20% of Corporate clients generate 75% of the overall gross margin.
- **Geographical Optimization:** The Southern region requires a logistics overhaul due to high shipping costs eroding profitability.

## 🚀 How to Run
1. Run `notebooks/2_Data_Cleaning_EDA.py` to preprocess the raw data.
2. Load the cleaned data into your SQL database and run the queries in `sql/3_Advanced_Analysis.sql`.
3. Open `powerbi/Dashboard.pbix` (conceptual) and refresh the data source to view the dashboards.

---
*Designed for scalable enterprise decision-making.*
