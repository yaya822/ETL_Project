import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
os.getcwd()
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")
db_host = os.getenv("DB_HOST","datahub-mysql-1")
import logging

logger = logging.getLogger(__name__)


def connect_to_mysql():
    try:
        engine = create_engine(
            f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )

        return engine

    except:
        logger.error("ERROR IN CONNECTION WITH DATABASE")
        raise ValueError("ERROR IN CONNECTION WITH DATABASE")




def extract_data(engine):
    with engine.connect() as conn:
        customers_df = pd.read_sql("SELECT * FROM customers", conn)
        vendor_df = pd.read_sql("SELECT * FROM vendor", conn)
        employee_df = pd.read_sql("SELECT * FROM employee", conn)
        insurance_df = pd.read_sql("SELECT * FROM insurance ", conn)
    
    return customers_df, vendor_df, employee_df, insurance_df


logging.info(
    "Extraction finished with succes ",
)
print("EXTRACTION DONE")
