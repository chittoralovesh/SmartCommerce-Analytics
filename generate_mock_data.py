import pandas as pd
import numpy as np
from datetime import timedelta, date
import random

def generate_mock_dataset():
    print("Generating 10,000 rows of realistic E-commerce data...")
    num_rows = 10000
    random.seed(42)
    np.random.seed(42)

    customers = [f"CUST-{i:04d}" for i in range(1, 501)]
    products = [f"PROD-{i:04d}" for i in range(1, 201)]
    categories = ["Technology", "Furniture", "Office Supplies"]
    sub_categories = {
        "Technology": ["Phones", "Accessories", "Machines", "Copiers"],
        "Furniture": ["Chairs", "Tables", "Bookcases", "Furnishings"],
        "Office Supplies": ["Paper", "Binders", "Art", "Storage"]
    }
    regions = ["North", "South", "East", "West"]
    shipping_modes = ["Standard Class", "First Class", "Second Class", "Same Day"]

    data = []
    start_date = date(2023, 1, 1)

    for i in range(num_rows):
        order_id = f"ORD-{random.randint(10000, 99999)}"
        customer = random.choice(customers)
        product = random.choice(products)
        category = random.choice(categories)
        sub_category = random.choice(sub_categories[category])
        region = random.choice(regions)
        shipping_mode = random.choice(shipping_modes)
        
        order_date = start_date + timedelta(days=random.randint(0, 365))
        ship_date = order_date + timedelta(days=random.randint(1, 7))
        
        quantity = random.randint(1, 10)
        sales = round(random.uniform(20.0, 1500.0), 2)
        discount = round(random.choice([0.0, 0.0, 0.1, 0.2, 0.3, 0.5]), 2)
        
        # Realistic profit calculation (higher discounts = lower/negative profit)
        cost_of_goods = sales * random.uniform(0.4, 0.7)
        revenue_after_discount = sales * (1 - discount)
        profit = round(revenue_after_discount - cost_of_goods, 2)
        
        data.append([
            order_id, customer, product, category, sub_category, region, shipping_mode, 
            order_date, ship_date, quantity, sales, discount, profit
        ])

    df = pd.DataFrame(data, columns=[
        "Order_ID", "Customer_ID", "Product_ID", "Category", "Sub_Category", "Region", "Shipping_Mode",
        "Order_Date", "Ship_Date", "Quantity", "Sales", "Discount", "Profit"
    ])

    df.to_csv("ecommerce_data.csv", index=False)
    print("Successfully created 'ecommerce_data.csv' with 10000 records!")

if __name__ == "__main__":
    generate_mock_dataset()
