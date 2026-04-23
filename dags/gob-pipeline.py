from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def job1():
    print("Job1 running")

def job2():
    print("Job2 running")

def job3():
    print("Job3 running")

def job4():
    print("Job4 running")

def job5():
    print("Job5 running")

def job6():
    print("Job6 running")

with DAG(
    dag_id="job_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="job1", python_callable=job1)
    t2 = PythonOperator(task_id="job2", python_callable=job2)
    t3 = PythonOperator(task_id="job3", python_callable=job3)
    t4 = PythonOperator(task_id="job4", python_callable=job4)
    t5 = PythonOperator(task_id="job5", python_callable=job5)
    t6 = PythonOperator(task_id="job6", python_callable=job6)

    t1 >> [t2, t3]
    t2 >> t4
    t3 >> t5
    [t4, t5] >> t6