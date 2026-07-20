import pandas as pd
from sqlalchemy import create_engine
import os 
from dotenv import load_dotenv
load_dotenv()
db_password=os.getenv("DB_PASSWORD")
db_driver=os.getenv("DB_DRIVER")
db_user=os.getenv("DB_USER")
db_name=os.getenv("DB_NAME")


# read data from csvs files 
employee_df = pd.read_csv("employee_data.csv")
vendor_df = pd.read_csv("vendor_data.csv")
insurance_df=pd.read_csv("insurance_data.csv")

# check dataframes 
employee_df
vendor_df
insurance_df

#create customers  dataframe 
customers_df=insurance_df[["CUSTOMER_ID","CUSTOMER_NAME","SSN","AGE","CUSTOMER_EDUCATION_LEVEL","ADDRESS_LINE1","ADDRESS_LINE2","CITY","POSTAL_CODE","MARITAL_STATUS","NO_OF_FAMILY_MEMBERS","EMPLOYMENT_STATUS","HOUSE_TYPE"]]

# delete columns from dataframes 
insurance_df=insurance_df.drop(columns=["CUSTOMER_NAME","SSN","AGE","CUSTOMER_EDUCATION_LEVEL","ADDRESS_LINE1","ADDRESS_LINE2","CITY","POSTAL_CODE","MARITAL_STATUS","NO_OF_FAMILY_MEMBERS","HOUSE_TYPE","EMPLOYMENT_STATUS"])
del vendor_df["STATE"]
del employee_df["STATE"]


# check dataframes 
employee_df.head()
vendor_df.head()
insurance_df.head()
customers_df.head()
customers_df.to_csv("customers.csv",index=False)

# connect to mysql 
# engine = create_engine(f"{db_driver}://{db_user}:{db_user}@localhost/{db_name}")

# # insert dataframes as tables to mysql
# with engine.connect() as conn:
#     customers_df.to_sql("customers", con=conn, if_exists="replace", index=False)
#     employee_df.to_sql("employee", con=conn, if_exists="replace", index=False)
#     vendor_df.to_sql("vendor", con=conn, if_exists="replace", index=False)
#     insurance_df.to_sql("insurance", con=conn, if_exists="replace", index=False)


len(customers_df)
new_customers_df=customers_df.dropna()
len(new_customers_df)






