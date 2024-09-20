from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import boto3
import pandas as pd

# AWS credentials
s3 = boto3.client('s3')

def download_data():
    # Download CIFAR-10 dataset or use Kaggle API
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    pd.DataFrame(X_train).to_csv('/tmp/X_train.csv')
    pd.DataFrame(y_train).to_csv('/tmp/y_train.csv')

def upload_to_s3():
    # Upload to AWS S3
    s3.upload_file('/tmp/X_train.csv', 'your-s3-bucket', 'X_train.csv')
    s3.upload_file('/tmp/y_train.csv', 'your-s3-bucket', 'y_train.csv')

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

with DAG(dag_id='data_ingestion', default_args=default_args, schedule_interval='@daily') as dag:
    task1 = PythonOperator(
        task_id='download_data',
        python_callable=download_data
    )
    task2 = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3
    )

    task1 >> task2

