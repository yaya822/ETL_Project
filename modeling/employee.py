import pandas as pd
import random 

employee_db=pd.read_csv("../insert_to_mysql/employee_data.csv")
employee_db.head()

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

del employee_db["ADDRESS_LINE2"]
del employee_db["STATE"]


name_mapping={}
for name in employee_db["AGENT_NAME"].unique():
    name_mapping[name]=random.choice(first_names)+" "+random.choice(last_names)

employee_db["AGENT_NAME"]=employee_db["AGENT_NAME"].map(name_mapping)


employee_db["CITY"]=employee_db["CITY"].replace(city_mapping)


name_mapping={}
for name in employee_db["AGENT_NAME"].unique():
    name_mapping[name]=random.choice(first_names)+random.choice(last_names)

employee_db["AGENT_NAME"]=employee_db["AGENT_NAME"].map(name_mapping)

address_mapping={}
for address in employee_db["ADDRESS_LINE1"]:
    address_mapping[address]=str(random.randrange(1,20))+" "+random.choice(street_types)+" "+random.choice(street_name)
    
employee_db["ADDRESS_LINE1"]=employee_db["ADDRESS_LINE1"].map(address_mapping)


employee_db["POSTAL_CODE"]=employee_db["CITY"].map(postal_codes)
employee_db.to_csv("../data/agent.csv")
