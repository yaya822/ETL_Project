import pandas as pd
from sqlalchemy import create_engine
import sys

sys.path.append("/home/guest/Desktop/ETL")
from extract_phase.extract import extract_data, connect_to_mysql
from extract_phase.validate import validate
from transform_phase.transform import (
    transform_employee,
    transform_insurance,
    transform_vendor,
    transfrom_customer,
)

import os 


def load():
    engine =connect_to_mysql()
    print(engine)
    customer,vendor,employee,insurance= extract_data(engine)
    customer,vendor,employee,insurance=validate(customer,vendor,employee,insurance)
    customer=transfrom_customer(customer)
    vendor=transform_vendor(vendor)
    employee=transform_employee(employee)
    insurance=transform_insurance(insurance)

    engine=create_engine(f"mysql+pymysql://yahya:YAHYA@172.18.0.6:3306/comfirmed_cleaned_db")
    type(engine)
    with engine.connect() as conn:
        customer.to_sql("customers_confirmed",con=conn,if_exists="replace",index=False)
        vendor.to_sql("vendors_confirmed",con=conn,if_exists="replace",index=False)
        employee.to_sql("employees_confirmed",con=conn,if_exists="replace",index=False)
        customer.to_sql("insurance_confirmed",con=conn,if_exists="replace",index=False)
load()