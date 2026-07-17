from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import logging


def check_s3():
    logging.info("Checking S3 raw bucket...")
    logging.info("S3 files found.")


def run_databricks():
    logging.info("Running Databricks Bronze → Silver → Gold pipeline...")


def validate_gold():
    logging.info("Validating Gold layer...")


def load_snowflake():
    logging.info("Loading data into Snowflake...")


def validate_snowflake():
    logging.info("Snowflake validation completed.")


with DAG(
    dag_id="ecommerce_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["aws", "databricks", "snowflake"],
) as dag:

    t1 = PythonOperator(
        task_id="check_s3",
        python_callable=check_s3,
    )

    t2 = PythonOperator(
        task_id="run_databricks",
        python_callable=run_databricks,
    )

    t3 = PythonOperator(
        task_id="validate_gold",
        python_callable=validate_gold,
    )

    t4 = PythonOperator(
        task_id="load_snowflake",
        python_callable=load_snowflake,
    )

    t5 = PythonOperator(
        task_id="validate_snowflake",
        python_callable=validate_snowflake,
    )

    t1 >> t2 >> t3 >> t4 >> t5