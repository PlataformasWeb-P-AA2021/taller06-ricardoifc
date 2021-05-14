from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_base import Paises 

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad docentes 
pais = session.query(Paises).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentar los países de Asía, ordenados por el atributo Dial")

paisAsia = session.query(Paises).filter(Paises.continente=="AS").order_by(Paises.dial).all() 
for p in paisAsia:
    print(p.nombre)
