import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.email import send_email

sys.path.append("/opt/airflow/ETL")
sys.path.append("/home/guest/Desktop/ETL")

import logging
import os

from dotenv import load_dotenv
from extract_phase.extract import connect_to_mysql, extract_data
from extract_phase.validate import validate
from load_phase.load import load
from transform_phase.transform import (
    transform_employee,
    transform_insurance,
    transfrom_customer,
)

load_dotenv()
db_host = os.getenv("DB_HOST", "127.0.0.1")

logger = logging.getLogger(__name__)


def success_email_notifier(context):
    subject = f"SUCCESS: DAG {context['dag'].dag_id} executed"
    html_content = f"""
    <h3>DAG Execution Successful</h3>
    <p><b>DAG ID:</b> {context["dag"].dag_id}</p>
    <p><b>Execution Date:</b> {context["ds"]}</p>
    """
    send_email(
        to=["bachri.yahya1869.ensa@uhp.ac.ma"],
        subject=subject,
        html_content=html_content,
    )


def connect_to_db():
    print("Connecting to db...")
    logger.info("Connecting to db...")
    return connect_to_mysql()


def extract():
    engine = connect_to_db()
    print("Extracting data ....")
    logger.info("Extracting data ....")
    return extract_data(engine)


def validate_data():
    engine = connect_to_db()
    customers, vendor, employee, insurance = extract_data(engine)
    print("Validate data")
    logger.info("Validate data...")
    return validate(customers, vendor, employee, insurance)


def transform():
    print("Transforming_data ...")
    logger.info("Tranforming data ...")
    customers, vendor, employee, insurance = validate_data()
    customers = transfrom_customer(customers)
    employee = transform_employee(employee)
    # vendor = transform_vendor(vendor)
    insurance = transform_insurance(insurance)
    return customers, employee, vendor, insurance


def load_to_db():
    print("Loading data ...")
    logger.info("Loading data ...")
    load()


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["bachri.yahya1869.ensa@uhp.ac.ma"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
with DAG(
    dag_id="etl_dag",
    start_date=datetime(2026, 8, 4),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    on_success_callback=success_email_notifier,
) as dag:
    connect_to_db_task = PythonOperator(
        task_id="connect_to_db_task",
        python_callable=connect_to_db,
        do_xcom_push=False,
    )
    extract_task = PythonOperator(
        task_id="extract_phase",
        python_callable=extract,
    )
    validation_task = PythonOperator(
        task_id="validation_data",
        python_callable=validate_data,
    )
    transform_task = PythonOperator(
        task_id="transform_phase",
        python_callable=transform,
    )
    load_to_db_task = PythonOperator(
        task_id="load_to_db_task",
        python_callable=load_to_db,
    )

    (
        connect_to_db_task
        >> extract_task
        >> validation_task
        >> transform_task
        >> load_to_db_task
    )

print(" Tasks DONE !!")
