import logging
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd

from extract_phase.extract import connect_to_mysql, extract_data

conn = connect_to_mysql()
customers, vendor, employee, insurance = extract_data()

logger = logging.getLogger(__name__)


def validate(customers, vendor, employee, insurance):
    logger.info("Validation started")

    logger.info("Checking for empty DataFrames...")
    if customers.empty or vendor.empty or employee.empty or insurance.empty:
        logger.error("One or more extracted DataFrames are empty.")
        raise ValueError("One or more extracted DataFrames are empty.")
    
    nbr_rows_customers = pd.read_sql("select count(*) from customers", conn)["count(*)"].iloc[0]

    nbr_rows_vendor = pd.read_sql("select count(*) from vendor", conn)["count(*)"].iloc[0]
    nbr_rows_employee = pd.read_sql("select count(*) from   employee", conn)["count(*)"].iloc[0]
    nbr_rows_insurance = pd.read_sql("select count(*) from  insurance", conn)["count(*)"].iloc[0]

    logger.info("Checking extracted rows counts... ")
    if (
        nbr_rows_vendor != len(vendor)
        or nbr_rows_customers != len(customers)
        or nbr_rows_employee != len(employee)
        or nbr_rows_insurance != len(insurance)
    ):
        logger.error("Failed to extract all rows ")
        raise ValueError("Failed to extract all rows ")

    db_customer_columns = pd.read_sql("describe customers", conn)
    db_vendor_columns = pd.read_sql("describe vendor", conn)
    db_employe_columns = pd.read_sql("describe employee", conn)
    db_insurance_columns = pd.read_sql("describe insurance", conn)

    logger.info("Checking extracted columns counts... ")

    if (
        db_customer_columns["Field"].to_list() != customers.columns.to_list()
        or db_vendor_columns["Field"].to_list() != vendor.columns.to_list()
        or db_employe_columns["Field"].to_list() != employee.columns.to_list()
        or db_insurance_columns["Field"].to_list() != insurance.columns.to_list()
    ):
        logger.error("Failed to extract all Columns")
        raise ValueError("Failed to extract all Columns ")

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

    def validate_dtypes(df,describe_df):
        expected_type = []
        actual_type = []
        
        for column in describe_df["Type"]:
                base_type = column.split("(")[0].strip().lower()
        
                pandas_type = mysql_to_pandas.get(base_type, "object")
        
                expected_type.append(pandas_type)
        
        for column in df.columns:
                dtype_str = str(df[column].dtype)
                actual_type.append(dtype_str)
        if actual_type != expected_type:
                logger.error("Different datatype extracted ")
                raise ValueError("Different datatype extracted ")

    logger.info("Checking Data type ... ")

    validate_dtypes(customers,db_customer_columns)
    validate_dtypes(employee,db_employe_columns)
    validate_dtypes(vendor,db_vendor_columns)
    validate_dtypes(insurance,db_insurance_columns)


    # check unicite of primary key in each tables
    logger.info("Checking Unicite of primary key ... ")

    if len(customers["CUSTOMER_ID"].unique()) != len(customers):
        logger.error("Validation failed: found  duplicate customer IDs.")
        raise ValueError("Validation failed: found  duplicate customer IDs.")

    if len(vendor["VENDOR_ID"].unique()) != len(vendor):
        logger.error("Validation failed: found  duplicate vendor IDs.")
        raise ValueError("Validation failed: found  duplicate vendor IDs.")

    if len(employee["AGENT_ID"].unique()) != len(employee):
        logger.error("Validation failed: found  duplicate agent  IDs.")
        raise ValueError("Validation failed: found  duplicate agent  IDs.")

    if len(insurance["TRANSACTION_ID"].unique()) != len(insurance):
        logger.error("Validation failed: found  duplicate insurance IDs.")
        raise ValueError("Validation failed: found  duplicate insurance IDs.")


    logger.info("Validation completed successfully.")