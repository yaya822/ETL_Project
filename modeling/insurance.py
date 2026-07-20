import pandas as pd 

insurance_db=pd .read_csv("../insert_to_mysql/insurance_data.csv")
insurance_db.head()

del insurance_db["INCIDENT_STATE"]

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

insurance_db["INCIDENT_CITY"]=insurance_db["INCIDENT_CITY"].replace(city_mapping)
insurance_db.to_csv("../data/insurance.csv")