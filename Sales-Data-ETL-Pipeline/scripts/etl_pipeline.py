# scripts/etl_pipeline.py
import pandas as pd
from sqlalchemy import create_engine

# Step 1: Extract - Load data from CSV
def extract_data(file_path):
    df = pd.read_csv(file_path)
    print("Data extracted successfully!")
    return df

# Step 2: Transform - Calculate total sales
def transform_data(df):
    df['TotalSales'] = df['Quantity'] * df['Price']
    print("Data transformed successfully!")
    return df

# Step 3: Load - Save data to SQLite database
def load_data(df, database_path, table_name):
    engine = create_engine(f'sqlite:///{database_path}')
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print("Data loaded successfully!")

# Main function
def main():
    # File paths
    input_file = r'C:\Users\phyzi\Sales-Data-ETL-Pipeline\data\sales_data.csv'  # Corrected file path
    database_path = r'C:\Users\phyzi\Sales-Data-ETL-Pipeline\database\sales.db'  # Corrected database path
    table_name = 'sales'  # Name of the table in the database

    # ETL process
    data = extract_data(input_file)
    transformed_data = transform_data(data)
    load_data(transformed_data, database_path, table_name)

if __name__ == "__main__":
    main()
