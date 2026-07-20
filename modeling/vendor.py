import pandas as pd
import random

vendor_db=pd.read_csv("../insert_to_mysql/vendor_data.csv")
vendor_db.head()

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
    "Livermore": "Taourirt",
    "Union City": "Midelt",
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
    "Litchfield Park": "Dakhla",
    "Saint Albans City": "Laayoune",
    "Medford": "Chefchaouen",
    "Cambridge": "Larache",
    "Hanover": "Taza",
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
del vendor_db["ADDRESS_LINE2"]
del vendor_db["STATE"]
mapping_name={}
for name in vendor_db["VENDOR_NAME"].unique():
    mapping_name[name] = random.choice(first_names) + " " + random.choice(last_names)

vendor_db["VENDOR_NAME"]=vendor_db["VENDOR_NAME"].map(mapping_name)

vendor_db["CITY"]=vendor_db["CITY"].replace(city_mapping)

mapping_address={}
for address in vendor_db["ADDRESS_LINE1"].unique():
    mapping_address[address]=str(random.randrange(1,50))+" "+random.choice(street_types)+" "+random.choice(street_name)
    print(mapping_address)


vendor_db["ADDRESS_LINE1"]=vendor_db["ADDRESS_LINE1"].map(mapping_address)

vendor_db.to_csv("../data/vendor.csv")
