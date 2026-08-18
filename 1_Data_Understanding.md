# Step 1: Data Understanding

## Dataset Structure & Important Columns
- **Order ID** (String): Unique identifier for each order.
- **Order Date / Ship Date** (Date): Used for time-series analysis and shipping duration calculations.
- **Customer ID / Customer Name** (String): Essential for customer segmentation and retention analysis.
- **Segment** (String): Consumer, Corporate, or Home Office.
- **Product ID / Product Name** (String): Item details for product analytics.
- **Category / Sub-Category** (String): Product classification.
- **Region / State / City** (String): Geographical sales mapping.
- **Sales** (Float): Revenue generated.
- **Quantity** (Integer): Number of units sold.
- **Discount** (Float): Discount percentage applied.
- **Profit** (Float): Net profit from the sale.
- **Shipping Mode** (String): Class of shipping (First Class, Standard, etc.).

## Data Quality Checks (Identifying Issues)
- **Missing Values:** Typically found in demographic fields (e.g., Postal Code) or optional customer details.
- **Duplicate Records:** Accidental double entries of Order IDs and Product IDs.
- **Data Inconsistencies:** Negative quantities or profits where illogical; mismatched date formats (e.g., MM/DD vs DD/MM).
- **Outliers:** Unusually high sales or bulk orders causing skewness in average order value.

## Data Cleaning Strategy
1. Standardize date formats using pandas `to_datetime`.
2. Fill or drop missing values (e.g., infer missing Postal Codes based on City/State).
3. Drop exact duplicate rows.
4. Cap or transform outliers using the IQR method for statistical modeling.

## Business-Focused KPIs
- **Gross Revenue & Net Profit**
- **Average Order Value (AOV)**
- **Customer Lifetime Value (CLV)**
- **Profit Margin %**
- **Year-over-Year (YoY) Sales Growth**
