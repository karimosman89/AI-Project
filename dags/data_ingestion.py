from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

dag = DAG(
    'data_ingestion',
    default_args=default_args,
    schedule_interval='@daily'
)

# Download CIFAR-10 data
download_data = BashOperator(
    task_id='download_cifar10',
    bash_command="curl -o /data/raw/train.7z <CIFAR-10-dataset-url>",
    dag=dag
)

# Extract train and test images
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='7z x /data/raw/train.7z -o/data/raw/',
    dag=dag
)

download_data >> extract_data

