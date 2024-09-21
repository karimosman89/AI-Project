from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
import requests
import zipfile

def download_data():
    url = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
    data_path = "/opt/airflow/data/raw/"
    
    os.makedirs(data_path, exist_ok=True)
    response = requests.get(url, stream=True)
    with open(os.path.join(data_path, "cifar-10-python.tar.gz"), "wb") as file:
        file.write(response.content)

    with zipfile.ZipFile(os.path.join(data_path, "cifar-10-python.tar.gz"), "r") as zip_ref:
        zip_ref.extractall(data_path)

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "data_ingestion",
    default_args=default_args,
    description="Ingest CIFAR-10 dataset",
    schedule_interval=timedelta(days=1),
)

download_task = PythonOperator(
    task_id="download_data",
    python_callable=download_data,
    dag=dag,
)

