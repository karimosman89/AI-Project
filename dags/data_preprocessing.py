from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data():
    # Load data
    df_train = pd.read_csv('/tmp/X_train.csv')
    
    # Data normalization
    scaler = StandardScaler()
    df_train = scaler.fit_transform(df_train)
    
    # Save preprocessed data
    pd.DataFrame(df_train).to_csv('/tmp/X_train_preprocessed.csv')

def upload_preprocessed_to_s3():
    s3.upload_file('/tmp/X_train_preprocessed.csv', 'your-s3-bucket', 'X_train_preprocessed.csv')

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

with DAG(dag_id='data_preprocessing', default_args=default_args, schedule_interval='@daily') as dag:
    task1 = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data
    )
    task2 = PythonOperator(
        task_id='upload_preprocessed_to_s3',
        python_callable=upload_preprocessed_to_s3
    )

    task1 >> task2
