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
    # Task 1 (Upstream)
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "Task 1 completed"',
    )

    # Task 2 (Downstream of task1)
    task2 = BashOperator(
        task_id='task2',
        bash_command='echo "Task 2 completed"',
    )

    # Task 3 (Downstream of task2)
    task3 = BashOperator(
        task_id='task3',
        bash_command='echo "Task 3 completed"',
    )

    # Set task dependencies (task1 -> task2 -> task3)
    task1 >> task2 >> task3