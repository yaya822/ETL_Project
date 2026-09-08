from datetime import datetime

from airflow.decorators import dag, task


@dag(
    dag_id='hello_world22',
    start_date=datetime(2023, 1, 1),
    schedule='@once',
    catchup=False,
)
def hello_world_dag():
    @task
    def print_hello():
        print("Hello, World!")

    print_hello()

dag_instance = hello_world_dag()