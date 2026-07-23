import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()
# os.getcwd()
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

db_port = os.getenv("DB_PORT")



def connect_to_mysql():
    try:
        engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@172.18.0.2:{db_port}/{db_name}")
        
    except:
        print("ERROR IN CONNECTION WITH DATABASE")
    return engine


def extract_data():
    engine = connect_to_mysql()

    # read tables from database
    customers_df = pd.read_sql("SELECT * FROM customers", engine)
    vendor_df = pd.read_sql("SELECT * FROM vendor", engine)
    employee_df = pd.read_sql("SELECT * FROM employee", engine)
    insurance_df = pd.read_sql("SELECT * FROM insurance ", engine)

    return customers_df, vendor_df, employee_df, insurance_df 


