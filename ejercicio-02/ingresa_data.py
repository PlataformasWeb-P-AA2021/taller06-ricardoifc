
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_base import Paises
import requests, json

engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

r = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
json_data = r.json()
for d in json_data:
    p = Paises(nombre = d["CLDR display name"], capital = d["Capital"], continente = d["Continent"], \
        dial = d["Dial"], geoID = d['Geoname ID'], itu = d["ITU"], lenguajes = d["Languages"],\
        independiente = d["is_independent"])
    
    session.add(p)

# confirmar transacciones
session.commit()
