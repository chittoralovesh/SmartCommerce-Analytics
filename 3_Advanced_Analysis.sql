-- STEP 3: ADVANCED SQL ANALYSIS

-- 1. Total Revenue, Profit, and Profit Margin by Year and Month (Window Functions & Aggregation)
WITH MonthlyAggregates AS (
    SELECT 
        EXTRACT(YEAR FROM order_date) AS order_year,
        EXTRACT(MONTH FROM order_date) AS order_month,
        SUM(sales) AS total_sales,
        SUM(profit) AS total_profit
    FROM ecommercedata
    GROUP BY EXTRACT(YEAR FROM order_date), EXTRACT(MONTH FROM order_date)
)
SELECT 
    order_year,
    order_month,
    total_sales,
    total_profit,
    ROUND((total_profit / total_sales) * 100, 2) AS profit_margin_pct,
    LAG(total_sales) OVER(ORDER BY order_year, order_month) AS prev_month_sales
FROM MonthlyAggregates;

-- 2. Top 10 Best-Selling Products by Revenue and Quantity (Aggregation & Sorting)
SELECT 
    product_id,
    category,
    SUM(sales) AS total_revenue,
    SUM(quantity) AS total_units_sold
FROM ecommercedata
GROUP BY product_id, category
ORDER BY total_revenue DESC
LIMIT 10;

-- 3. Top High-Value Customers and Average Order Value (AOV)
SELECT 
    customer_id,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(sales) AS total_spent,
    SUM(sales) / COUNT(DISTINCT order_id) AS average_order_value
FROM ecommercedata
GROUP BY customer_id
HAVING SUM(sales) > 5000 -- Threshold for high value
ORDER BY total_spent DESC;

-- 4. Region-wise Performance & Ranking (Window Functions)
SELECT 
    region,
    SUM(sales) AS regional_sales,
    SUM(profit) AS regional_profit,
    RANK() OVER(ORDER BY SUM(sales) DESC) AS sales_rank
FROM ecommercedata
GROUP BY region;

-- 5. Customer Retention: First Purchase vs Latest Purchase (CTEs)
WITH CustomerLifespan AS (
    SELECT 
        customer_id,
        MIN(order_date) AS first_purchase,
        MAX(order_date) AS last_purchase,
        COUNT(DISTINCT order_id) AS order_count
    FROM ecommercedata
    GROUP BY customer_id
)
SELECT 
    customer_id,
    first_purchase,
    last_purchase,
    order_count,
    DATE_PART('day', last_purchase - first_purchase) AS days_retained
FROM CustomerLifespan
WHERE order_count > 1
ORDER BY days_retained DESC;

-- 6. Discount Impact Analysis
SELECT 
    CASE 
        WHEN discount = 0 THEN 'No Discount'
        WHEN discount > 0 AND discount <= 0.2 THEN 'Low (1-20%)'
        WHEN discount > 0.2 AND discount <= 0.4 THEN 'Medium (21-40%)'
        ELSE 'High (>40%)' 
    END AS discount_tier,
    COUNT(order_id) AS number_of_orders,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    AVG(profit) AS avg_profit_per_order
FROM ecommercedata
GROUP BY discount_tier
ORDER BY total_sales DESC;
