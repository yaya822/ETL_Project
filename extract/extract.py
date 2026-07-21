import pandas as pd
from dotenv import load_dotenv
import os
import mysql.connector
from sqlalchemy import create_engine

load_dotenv()
# os.getcwd()
db_name = os.getenv("DB_NAME")
db_name
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@127.0.0.1/{db_name}")
customers_df = pd.read_sql("SELECT * FROM customers", engine)
vendor_df = pd.read_sql("SELECT * FROM vendor", engine)
employee_df = pd.read_sql("SELECT * FROM employee", engine)
insurance_df = pd.read_sql("SELECT * FROM insurance ", engine)


customers_df.head()
insurance_df.head()
vendor_df.head()
employee_df.head()
