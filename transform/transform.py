from extract.extract import extract_data
from extract.validate import validate

customers, vendor, employee, insurance = extract_data()

# transform the customers table
customers.rename(columns={"SSN": "CIN"}, inplace=True)
customers.rename(columns={"ADDRESS_LINE1": "ADDRESS_LINE"}, inplace=True)


customers.head(30)
customers.fillna(
    {
        "POSTAL_CODE": 20220,
        "CUSTOMER_EDUCATION_LEVEL": "High School",
        "CITY": "Casablanca",
    },
    inplace=True,
)

customers.isnull().sum()

type(customers["POSTAL_CODE"][0])
# change datatype
customers = customers.astype({"POSTAL_CODE": int})
# check negative values
for c in customers["AGE"]:
    if c >= 0:
        print("negative age ")


for dp in customers.duplicated().to_list():
    if dp == True:
        print("duplicated rows ")
new_customers = customers.drop_duplicates()
len(customers) - len(new_customers)  # =0 so there is no duplicated rows
# transfrom the vendor

vendor.head(10)
vendor.rename(columns={"ADDRESS_LINE1": "ADDRESS_LINE"})

vendor.isnull().sum()
vendor.fillna({"CITY": "CASABLANCA"}, inplace=True)

for dp in vendor.duplicated().to_list():
    if dp == True:
        print("duplicated rows")


# tranform employee
employee.head()
employee.isnull().sum()
employee.fillna(
    {"POSTAL_CODE": 20220, "CITY": "Casablanca"},
    inplace=True,
)
employee.rename(columns={"ADDRESS_LINE1":"ADDRESS_LINE"},inplace=True)

for e in employee.duplicated().to_list():
    if e:
        print("duplicated rows ")

employee=employee.astype({"POSTAL_CODE":int})
employee
