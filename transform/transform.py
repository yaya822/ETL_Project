from extract.extract import extract_data
from extract.validate import validate
import datetime
customers, vendor, employee, insurance = extract_data()


# transform the customers table
customers.rename(columns={"SSN": "CIN"}, inplace=True)
customers.rename(columns={"ADDRESS_LINE1": "ADDRESS_LINE"}, inplace=True)
del customers["Unnamed: 0"]


customers.head(10)
customers.isnull().sum()
customers.dropna(subset=["CITY"], inplace=True)

mode = customers["CUSTOMER_EDUCATION_LEVEL"].mode()[0]
customers.fillna(
    {
        "POSTAL_CODE": 00000,
        "CUSTOMER_EDUCATION_LEVEL": mode,
    },
    inplace=True,
)

customers.isnull().sum()
customers

type(customers["POSTAL_CODE"][0])
# change datatype
customers = customers.astype({"POSTAL_CODE": int})
type(customers["POSTAL_CODE"][0])
# check negative values
for c in customers["AGE"]:
    if c <= 0:
        print("negative age ")


for dp in customers.duplicated().to_list():
    if dp == True:
        print("duplicated rows ")
new_customers = customers.drop_duplicates()
len(customers) - len(new_customers)
new_customers  # =0 so there is no duplicated rows


# transfrom the vendor
vendor.head(10)
vendor.rename(columns={"ADDRESS_LINE1": "ADDRESS_LINE"})

vendor.isnull().sum()
vendor.dropna(subset=["CITY"], inplace=True)

for dp in vendor.duplicated().to_list():
    if dp == True:
        print("duplicated rows")

new_vendor = vendor.drop_duplicates()
len(new_vendor)


# tranform employee
employee.isnull().sum()
employee.fillna({"POSTAL_CODE": 00000},inplace=True,)

employee.dropna(subset=["CITY"], inplace=True)
employee.rename(columns={"ADDRESS_LINE1": "ADDRESS_LINE"}, inplace=True)
employee.tail(10)
employee = employee.astype({"POSTAL_CODE": int})
for e in employee.duplicated().to_list():
    if e:
        print("duplicated rows ")

employee.head(10)
employee.drop(0)
del employee["Unnamed: 0"]
employee.head(10)

employee["DATE_OF_JOINING"]=employee["DATE_OF_JOINING"].datetime.date()




insurance.head(10)