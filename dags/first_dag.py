from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "code2j",
    "retries": 1,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id='first_dag',
    default_args=default_args,
    descirption='My first DAG',
    schedule_interval='@daily',
    start_date=datetime(2023, 10, 1),
) as dag:
    task_id="first_task"
    bash_command="echo 'Hello World'"