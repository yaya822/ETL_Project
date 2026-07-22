import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from extract.extract import extract_data, connect_to_mysql
import pandas as pd

customers, vendor, employee, insurance = extract_data()
conn = connect_to_mysql()


def validate(customers, vendor, employee, insurance):
    if customers.empty or vendor.empty or employee.empty or insurance.empty:
        print("EMPTY DATAFAMES ")
    nbr_rows_customers = pd.read_sql("select count(*) from customers", conn)
    nbr_rows_vendor = pd.read_sql("select count(*) vendor", conn)
    nbr_rows_employee = pd.read_sql("select count(*) employee", conn)
    nbr_rows_insurance = pd.read_sql("select count(*) insurance", conn)
    if (
        nbr_rows_vendor != len(vendor)
        or nbr_rows_customers != len(customers)
        or nbr_rows_employee != len(employee)
        or nbr_rows_insurance != len(insurance)
    ):
        print("ERROR: MISSING ROWS")

    db_customer_columns = pd.read_sql("describe customers", conn)
    db_vendor_columns = pd.read_sql("describe vendor", conn)
    db_employe_columns = pd.read_sql("describe employee", conn)
    db_insurance_columns = pd.read_sql("describe insurance", conn)

    if (
        db_customer_columns["Field"].to_list() != customers.columns.to_list()
        or db_vendor_columns["Field"].to_list() != vendor.columns.to_list()
        or db_employe_columns["Field"].to_list() != employee.columns.to_list()
        or db_insurance_columns["Field"].to_list() != insurance.columns.to_list()
    ):
        print("ERROR:MISSING COLUMN ")

    # verifie datatype
    mysql_to_pandas = {
        "varchar": "object",
        "text": "object",
        "int": "int64",
        "bigint": "int64",
        "double": "float64",
        "float": "float64",
        "date": "datetime64[ns]",
        "datetime": "datetime64[ns]",
    }

    expected_type = []
    actual_type = []

    for column in db_customer_columns["Type"]:
        base_type = column.split("(")[0].strip().lower()

        pandas_type = mysql_to_pandas.get(base_type, "object")

        expected_type.append(pandas_type)

    for column in customers.columns:
        dtype_str = str(customers[column].dtype)
        actual_type.append(dtype_str)

    if actual_type != expected_type:
        print("DIFFERENT DATATYPE IN CUSTOMERS TABLE")

    expected_type = []
    actual_type = []

    for column in db_vendor_columns["Type"]:
        base_type = column.split("(")[0].strip().lower()

        pandas_type = mysql_to_pandas.get(base_type, "object")

        expected_type.append(pandas_type)

    for column in vendor.columns:
        dtype_str = str(vendor[column].dtype)
        actual_type.append(dtype_str)
    if actual_type != expected_type:
        print("DIFFERENT DATATYPE IN VENDOR TABLE")

    expected_type = []
    actual_type = []

    for column in db_employe_columns["Type"]:
        base_type = column.split("(")[0].strip().lower()

        pandas_type = mysql_to_pandas.get(base_type, "object")

        expected_type.append(pandas_type)

    for column in employee.columns:
        dtype_str = str(employee[column].dtype)
        actual_type.append(dtype_str)
    if actual_type != expected_type:
        print("DIFFERENT DATATYPE IN EMPLOYEE TABLE")

    expected_type = []
    actual_type = []

    for column in db_insurance_columns["Type"]:
        base_type = column.split("(")[0].strip().lower()

        pandas_type = mysql_to_pandas.get(base_type, "object")

        expected_type.append(pandas_type)

    for column in insurance.columns:
        dtype_str = str(insurance[column].dtype)
        actual_type.append(dtype_str)
    if actual_type != expected_type:
        print("DIFFERENT DATATYPE IN INSURANCE TABLE")

    # check unicite of primary key in each tables 


