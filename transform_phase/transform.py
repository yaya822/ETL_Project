import sys

sys.path.append("/home/guest/Desktop/ETL")

import pandas as pd


# transform the customers table
def transfrom_customer(customers):

    customers.rename(columns={"SSN": "CIN"}, inplace=True)
    customers.rename(columns={"ADDRESS_LINE1": "ADDRESS_LINE"}, inplace=True)
    del customers["Unnamed: 0"]

    customers.head(10)
    customers.isnull().sum()
    customers.dropna(subset=["CITY"], inplace=True)

    mode = customers["CUSTOMER_EDUCATION_LEVEL"].mode()[0]
    customers.fillna(
        {
            "POSTAL_CODE": 0,
            "CUSTOMER_EDUCATION_LEVEL": mode,
        },
        inplace=True,
    )

    customers.isnull().sum()

    type(customers["POSTAL_CODE"][0])
    # change datatype
    customers = customers.astype({"POSTAL_CODE": int})
    type(customers["POSTAL_CODE"][0])
    # check negative values
    invalide_age = customers[customers["AGE"] <= 0]
    print(f"{len(invalide_age)} ivalide age ")

    for dp in customers.duplicated().to_list():
        if dp == True:
            print("duplicated rows ")
    new_customers = customers.drop_duplicates()
    len(customers) - len(new_customers)
    return new_customers


# transfrom the vendor
def transform_vendor(vendor):
    vendor.head(10)
    vendor.rename(columns={"ADDRESS_LINE1": "ADDRESS_LINE"}, inplace=True)

    vendor.isnull().sum()
    vendor.dropna(subset=["CITY"], inplace=True)
    del vendor["Unnamed: 0"]

    duplicates_rows = vendor.duplicated().sum()
    print(f"{duplicates_rows} duplicated rows")

    new_vendor = vendor.drop_duplicates()
    len(new_vendor)
    return new_vendor


# tranform employee
def transform_employee(employee):
    employee.isnull().sum()
    employee.fillna(
        {"POSTAL_CODE": 00000},
        inplace=True,
    )

    employee.dropna(subset=["CITY"], inplace=True)
    employee.rename(columns={"ADDRESS_LINE1": "ADDRESS_LINE"}, inplace=True)
    employee.tail(10)
    employee = employee.astype({"POSTAL_CODE": int})
    for e in employee.duplicated().to_list():
        if e:
            print("duplicated rows ")

    employee.head(10)
    employee.drop(index=0, inplace=True)
    del employee["Unnamed: 0"]
    employee.head(10)

    employee["DATE_OF_JOINING"] = pd.to_datetime(employee["DATE_OF_JOINING"])
    employee["DATE_OF_JOINING"] = employee["DATE_OF_JOINING"] + pd.DateOffset(years=10)
    employee.head()
    return employee


def transform_insurance(insurance):
    insurance.dropna(subset=["INCIDENT_CITY"], inplace=True)
    insurance.isnull().sum()
    insurance.fillna(
        {"AUTHORITY_CONTACTED": "No one ", "VENDOR_ID": 00000}, inplace=True
    )

    insurance.head(10)
    insurance["TXN_DATE_TIME"] = pd.to_datetime(
        insurance["TXN_DATE_TIME"]
    ) + pd.DateOffset(years=3)
    insurance["POLICY_EFF_DT"] = pd.to_datetime(
        insurance["POLICY_EFF_DT"]
    ) + pd.DateOffset(years=5)
    insurance["LOSS_DT"] = pd.to_datetime(insurance["LOSS_DT"]) + pd.DateOffset(years=3)
    insurance["REPORT_DT"] = pd.to_datetime(insurance["REPORT_DT"]) + pd.DateOffset(
        years=3
    )

    insurance.columns.to_list()
    del insurance["TENURE"]
    del insurance["SOCIAL_CLASS"]

    insurance.head(10)

    return insurance


