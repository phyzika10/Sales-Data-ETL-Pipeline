# Sales Data ETL Pipeline

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline for analyzing sales data.

## Project Structure
- `data/`: Contains the raw CSV data.
- `scripts/`: Contains Python scripts for the ETL pipeline and data analysis.
- `database/`: Contains the SQLite database.
- `README.md`: Project documentation.

## Steps
1. **Extract**: Load data from `sales_data.csv`.
2. **Transform**: Calculate total sales for each order.
3. **Load**: Save the transformed data into a SQLite database.
4. **Analyze**: Query the database and visualize total sales by product.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt