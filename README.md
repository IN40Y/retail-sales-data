# Interactive Retail Data Dashboard

This project demonstrates a retail sales data pipeline and an interactive dashboard for real-time business insights.

## Project Overview:
- **Retail Sales Data Simulation**: A sizeable dataset of 50,000 sales records is generated using the `faker` library. The dataset includes transactions, products, categories, and regions.
- **Data Pipeline**: Built using Apache Airflow, the pipeline automates the daily ETL process to load data into a PostgreSQL database.
- **Interactive Dashboard**: Developed using Dash and Plotly to visualize sales data trends, category performance, and regional analysis.

## Features:
- Real-time updates through Airflow
- Sales trends over time
- Sales comparison by product category
- Regional sales performance

## Getting Started:
1. Clone the repository: `git clone https://github.com/IN40Y/retail-sales-data.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up PostgreSQL database for the pipeline.
4. Run the Airflow scheduler.
5. Launch the dashboard: `python app.py`

## Datasets:
- **`retail_sales_data.csv`**: A synthetic dataset of retail sales transactions.
