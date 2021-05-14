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
print("Presentar todos los países que tengan en su cadena de nombre de país 'uador' o en su cadena de capital 'ito'")

pais = session.query(Paises).filter(or_(Paises.nombre.like("%uador"),Paises.capital.like("%ito"))).all() 
for p in pais:
    print(str(p.nombre) + " - " + str(p.capital))
