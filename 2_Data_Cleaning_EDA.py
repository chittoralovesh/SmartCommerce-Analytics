import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set_theme(style="whitegrid")

# 1. Load Dataset
df = pd.read_csv('ecommerce_data.csv')

print("Loading dataset...")

# 2. Data Cleaning
def clean_data(df):
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # Handle Missing Values
    if 'postal_code' in df.columns:
        df['postal_code'] = df['postal_code'].fillna('Unknown')
    
    # Remove Duplicates
    df = df.drop_duplicates()
    
    # Convert Dates
    date_cols = ['order_date', 'ship_date']
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            
    # Handle Data Inconsistencies (e.g., negative quantities)
    df = df[df['quantity'] > 0]
    
    return df

# 3. Feature Engineering
def engineer_features(df):
    # Shipping Time (Days)
    df['shipping_duration'] = (df['ship_date'] - df['order_date']).dt.days
    
    # Year, Month, Day, Quarter for Time Series
    df['order_year'] = df['order_date'].dt.year
    df['order_month'] = df['order_date'].dt.month
    df['order_quarter'] = df['order_date'].dt.quarter
    
    # Profit Margin
    df['profit_margin'] = df['profit'] / df['sales']
    
    # Customer Segmentation (RFM basic structure)
    df['is_high_value'] = np.where(df['sales'] > df['sales'].quantile(0.75), 1, 0)
    
    return df

# 4. Exploratory Data Analysis (EDA) & Visualizations
def perform_eda(df):
    # Total Sales by Category
    plt.figure(figsize=(10, 6))
    sales_by_cat = df.groupby('category')['sales'].sum().sort_values(ascending=False)
    sns.barplot(x=sales_by_cat.index, y=sales_by_cat.values, palette='viridis', hue=sales_by_cat.index, legend=False)
    plt.title('Total Sales by Category')
    plt.ylabel('Sales ($)')
    plt.savefig('sales_by_category.png')
    plt.close()
    
    # Sales Trend over Time
    plt.figure(figsize=(12, 6))
    monthly_sales = df.groupby(df['order_date'].dt.to_period('M'))['sales'].sum()
    monthly_sales.plot(kind='line', marker='o')
    plt.title('Monthly Sales Trend')
    plt.ylabel('Sales ($)')
    plt.xlabel('Date')
    plt.savefig('monthly_sales_trend.png')
    plt.close()

    # Correlation Matrix
    numeric_df = df.select_dtypes(include=[np.number])
    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.savefig('correlation_matrix.png')
    plt.close()

# 5. Execution & Saving
if __name__ == "__main__":
    df_clean = clean_data(df)
    df_featured = engineer_features(df_clean)
    perform_eda(df_featured)
    df_featured.to_csv('cleaned_ecommerce_data.csv', index=False)
    print("Data cleaning complete. EDA visualisations saved as PNG files!")
