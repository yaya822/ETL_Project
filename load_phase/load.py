import sys

import pandas as pd
from sqlalchemy import create_engine

sys.path.append("/home/guest/Desktop/ETL")
import os

from dotenv import load_dotenv

from extract_phase.extract import connect_to_mysql, extract_data
from extract_phase.validate import validate
from transform_phase.transform import (
    transform_employee,
    transform_insurance,
    transform_vendor,
    transfrom_customer,
)

load_dotenv()
db_user=os.getenv("DB_USER")
db_password=os.getenv("DB_PASSWORD")
db_host=os.getenv("DATA_WHEREHOUSE")
db_name=os.getenv("DB_NAME")
print(db_host)




def load():
    engine =connect_to_mysql()
    print(engine)
    customer,vendor,employee,insurance= extract_data(engine)
    customer,vendor,employee,insurance=validate(customer,vendor,employee,insurance)
    customer=transfrom_customer(customer)
    vendor=transform_vendor(vendor)
    employee=transform_employee(employee)
    insurance=transform_insurance(insurance)

    engine=create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/comfirmed_cleaned_db")
    type(engine)
    with engine.connect() as conn:
        customer.to_sql("customers_confirmed",con=conn,if_exists="replace",index=False)
        vendor.to_sql("vendors_confirmed",con=conn,if_exists="replace",index=False)
        employee.to_sql("employees_confirmed",con=conn,if_exists="replace",index=False)
        insurance.to_sql("insurance_confirmed",con=conn,if_exists="replace",index=False)