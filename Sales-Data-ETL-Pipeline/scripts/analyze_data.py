# scripts/analyze_data.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Connect to the SQLite database
def query_data(database_path, table_name):
    engine = create_engine(f'sqlite:///{database_path}')
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    return df

# Analyze and visualize data
def analyze_data(df):
    # Total sales by product
    sales_by_product = df.groupby('Product')['TotalSales'].sum().reset_index()

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Product', y='TotalSales', data=sales_by_product)
    plt.title('Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.savefig(r'C:\Users\phyzi\Sales-Data-ETL-Pipeline\data\sales_by_product.png')  # Corrected file path
    plt.show()

# Main function
def main():
    database_path = r'C:\Users\phyzi\Sales-Data-ETL-Pipeline\database\sales.db'  # Corrected database path
    table_name = 'sales'

    data = query_data(database_path, table_name)
    analyze_data(data)

if __name__ == "__main__":
    main()
