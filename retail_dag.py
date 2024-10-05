from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import psycopg2

# ETL Function to ingest and load data into PostgreSQL
def load_retail_data():
    # Read CSV data
    df = pd.read_csv('retail_sales_data.csv')
    
    # Establish DB connection
    conn = psycopg2.connect(
        host="localhost",
        database="retail_db",
        user="your_user",
        password="your_password"
    )
    cursor = conn.cursor()
    
    # Insert data into PostgreSQL
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO retail_sales (transaction_id, date, store_id, product_id, category, region, price, quantity, total_sales)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))
    
    # Commit transaction
    conn.commit()
    cursor.close()
    conn.close()

# Define default arguments for DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'retail_data_pipeline',
    default_args=default_args,
    schedule_interval='@daily'
)

# Define tasks
load_data = PythonOperator(
    task_id='load_retail_data',
    python_callable=load_retail_data,
    dag=dag
)
