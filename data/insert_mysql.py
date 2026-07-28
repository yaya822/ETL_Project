import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
print(os.getcwd())

db_name = os.getenv("DB_NAME")
db_password = os.getenv("DB_PASSWORD")
db_driver = os.getenv("DB_DRIVER")
db_user = os.getenv("DB_USER")
db_port=os.getenv("DB_PORT")

print(db_driver)
print(db_user)
print(db_password)
print(db_name)

customers_df = pd.read_csv("../data/customers.csv")
insurance_df = pd.read_csv("../data/insurance.csv")
employee_df = pd.read_csv("../data/agent.csv")
vendor_df = pd.read_csv("../data/vendor.csv")





engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@172.18.0.2:{db_port}/{db_name}")


with engine.connect() as conn:
    #customers_df.to_sql("customers", con=conn, if_exists="replace", index=False)
    employee_df.to_sql("employee", con=conn, if_exists="replace", index=False)
    #vendor_df.to_sql("vendor", con=conn, if_exists="replace", index=False)
    # insurance_df.to_sql("insurance", con=conn, if_exists="replace", index=False)
