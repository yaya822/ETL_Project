import pandas as pd
import random

first_names = [
    "Ahmed",
    "Youssef",
    "Mohamed",
    "Omar",
    "Hassan",
    "Salma",
    "Fatima",
    "Khadija",
    "Aya",
    "Meryem",
    "Othmane",
    "Hamza",
    "Yahya",
    "Amine",
    "Youssef",
    "Omar",
    "Kawtar",
    "Kaoutar",
    "Hiba",
    "Hajar",
    "Mohammed Amine",
    "Taha",
    "Rachida",
    "Aziza",
    "Adam",
    "Fatima Ezzahra ",
    "Noha",
    "Zineb",
    "Rania",
    "Malak",
    "Jamila",
    "Khaoula",
]

last_names = [
    "Alaoui",
    "Benali",
    "El Idrissi",
    "Bennani",
    "Amrani",
    "Lahlou",
    "Tazi",
    "Berrada",
    "El Fassi",
    "Ouazzani",
    "Skalli",
    "Bachri",
    "El Yousfi",
    "Benchikh",
    "Amine",
    "Metouali",
    "Salhi",
    "Banoune",
    "Tahiri",
    "Kibala",
    "Radi",
    "Mansour",
    "Barghoud",
    "Bate",
    "Fadili",
    "Moufkir ",
    "Fakhir",
    "Dadi",
    "Mansar",
    "Farissi",
    "Jamal",
    "Eddoughmi",
    "Oufkir",
]


city_mapping = {
    "Montgomery": "Casablanca",
    "Fayetteville": "Rabat",
    "Washington": "Tanger",
    "Nashville": "Marrakech",
    "Arvada": "Agadir",
    "Manchester": "Sale",
    "Glendale": "Fes",
    "Louisville": "Meknes",
    "Anchorage": "Tetouan",
    "Savannah": "Kenitra",
    "Panama City": "Essaouira",
    "Oklahoma City": "Oujda",
    "Panama City Beach": "El Jadida",
    "Oakland": "Safi",
    "Glean Burnie": "Beni Mellal",
    "Fremont": "El Hoceima",
    "Annapolis": "Ouarzazate",
    "Hayward": "Guelmim",
    "Berkeley": "Nador",
    "Pooler": "Khourubga",
    "Pasadena": "Sefrou",
    "Lynn Haven": "Berrechid",
    "Edmond": "Settat",
    "San leandro": "Fnideq",
    "Livermore": "Laayoune",
    "Union City": "MideltDakhla",
    "Moore": "Berkane",
    "Severne": "Ifrane",
    "Norman": "Sidi Kacem",
    "Burlington": "Taaroudant",
    "Quincy": "El Kelaa des Sraghna",
    "Rutland": "Ben Guerir",
    "Groton": "Guercif",
    "Severna Park": "Mohammedia",
    "Farmington": "Tan Tan",
    "Edgwater": "Tiflet",
    "Cupernito": "Sidi Sliame",
    "Midwest City": "Azrou",
    "Castro Valley": "Oued Zem",
    "Hartford": "Tiznit",
    "Litchfield Park": "Midelt",
    "Saint Albans City": "Taourirt",
    "Medford": "Chefchaouen",
    "Cambridge": "Larache",
    "Hanover": "Taza",
}

postal_codes = {
    "Casablanca": 20220,
    "Rabat": 11025,
    "Tanger": 90053,
    "Marrakech": 40000,
    "Agadir": 80000,
    "Sale": 11000,
    "Fes": 30000,
    "Meknes": 50010,
    "Tetouan": 93000,
    "Kenitra": 14110,
    "Essaouira": 44000,
    "Oujda": 60010,
    "El Jadida": 24010,
    "Safi": 46000,
    "Beni Mellal": 23000,
    "El Hoceima": 32000,
    "Ouarzazate": 45000,
    "Guelmim": 81000,
    "Nador": 62000,
    "Khourubga": 25000,
    "Sefrou": 31000,
    "Berrechid": 26100,
    "Settat": 26000,
    "Fnideq": 93200,
    "Taourirt": 65000,
    "Midelt": 54350,
    "Berkane": 60300,
    "Ifrane": 53000,
    "Sidi Kacem": 16000,
    "Taaroudant": 83000,
    "El Kelaa des Sraghna": 43000,
    "Ben Guerir": 43150,
    "Guercif": 37000,
    "Mohammedia": 28810,
    "Tan Tan": 82000,
    "Tiflet": 15400,
    "Sidi Sliame": 14200,
    "Azrou": 53100,
    "Oued Zem": 25200,
    "Tiznit": 85000,
    "Dakhla": 73000,
    "Laayoune": 70000,
    "Chefchaouen": 91000,
    "Larache": 92000,
    "Taza": 35000,
}

cin_mapping = {
    "Casablanca": "BJ",
    "Rabat": "AG",
    "Tanger": "KB",
    "Marrakech": "EE",
    "Agadir": "JK",
    "Sale": "AB",
    "Fes": "CC",
    "Meknes": "DN",
    "Tetouan": "L",
    "Kenitra": "G",
    "Essaouira": "N",
    "Oujda": "F",
    "El Jadida": "M",
    "Safi": "HH",
    "Beni Mellal": "I",
    "El Hoceima": "R",
    "Ouarzazate": "P",
    "Guelmim": "JA",
    "Nador": "SA",
    "Khouribga": "Q",
    "Sefrou": "CB",
    "Berrechid": "WA",
    "Settat": "W",
    "Fnideq": "LF",
    "Taourirt": "FB",
    "Midelt": "VA",
    "Berkane": "FA",
    "Ifrane": "DB",
    "Sidi Kacem": "GK",
    "Taaroudant": "JC",
    "El Kelaa des Sraghna": "Y",
    "Ben Guerir": "EA",
    "Guercif": "ZG",
    "Mohammedia": "T",
    "Tan Tan": "JF",
    "Tiflet": "XA",
    "Sidi Sliame": "GA",
    "Azrou": "DA",
    "Oued Zem": "QA",
    "Tiznit": "JE",
    "Dakhla": "OD",
    "Laayoune": "SH",
    "Chefchaouen": "LC",
    "Larache": "LA",
    "Taza": "Z",
}
street_types=[
    "Avenue",
    "Rue",
    "Boulevard",
    "Lotissement",
    "Hay",
    "Residence"
]
street_name=[
    "Hlioua",
    "Bernoussi",
    "Salam",
    "Mohammed V",
    "Hassan II",
    "Al Massira",
    "Centrale",
    "Zerktouni",
    "Al Qods",
    "Al Houda",
    "El Fadl",
]
customers_df = pd.read_csv("../insert_to_mysql/customers.csv")

mapping_name = {}


# creating random names
for name in customers_df["CUSTOMER_NAME"].unique():
    mapping_name[name] = random.choice(first_names) + " " + random.choice(last_names)

# to change name
customers_df["CUSTOMER_NAME"] = customers_df["CUSTOMER_NAME"].map(mapping_name)
customers_df


# to change cities
customers_df["CITY"] = customers_df["CITY"].replace(city_mapping)
customers_df

del customers_df["ADDRESS_LINE2"]

customers_df["POSTAL_CODE"] = customers_df["CITY"].map(postal_codes)

mapping_cin = {}
ssn_to_city = (
    customers_df.drop_duplicates(subset=["SSN"]).set_index("SSN")["CITY"].to_dict()
)
ssn_to_city
for cin in customers_df["SSN"].unique():
    city = ssn_to_city.get(cin)
    letters = cin_mapping.get(city, "X")

    mapping_cin[cin] = letters + str(random.randrange(100000, 999999))

customers_df["SSN"] = customers_df["SSN"].map(mapping_cin)


mapping_address={}
for address in customers_df["ADDRESS_LINE1"].unique():
    mapping_address[address]=str(random.randrange(1,50))+" "+ random.choice(street_types)+" "+random.choice(street_name)

customers_df["ADDRESS_LINE1"]=customers_df["ADDRESS_LINE1"].map(mapping_address)

customers_df.to_csv("../data/customers.csv")
customers_df