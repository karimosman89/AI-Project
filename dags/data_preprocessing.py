from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import tensorflow as tf
import os

def preprocess_data():
    # Load dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

    # Normalize the images to [0, 1] range
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Save preprocessed data
    processed_data_path = "/opt/airflow/data/processed/"
    os.makedirs(processed_data_path, exist_ok=True)
    
    tf.data.experimental.save(x_train, os.path.join(processed_data_path, "x_train"))
    tf.data.experimental.save(y_train, os.path.join(processed_data_path, "y_train"))
    tf.data.experimental.save(x_test, os.path.join(processed_data_path, "x_test"))
    tf.data.experimental.save(y_test, os.path.join(processed_data_path, "y_test"))

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
    "data_preprocessing",
    default_args=default_args,
    description="Preprocess CIFAR-10 dataset",
    schedule_interval=timedelta(days=1),
)

preprocess_task = PythonOperator(
    task_id="preprocess_data",
    python_callable=preprocess_data,
    dag=dag,
)

