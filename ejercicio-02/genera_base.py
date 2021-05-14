from sqlalchemy import create_engine
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Paises(Base):
    __tablename__ = 'lospaises'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoID = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    independiente = Column(String)

    def __repr__(self):
        return "Paises: nombre=%s capital=%s continente:%s dial:%s geoID:%s itu:%s lenguajes:%s independiente:%s" % (
                          self.nombre, 
                          self.capital, 
                          self.continente,
                          self.dial,
                          self.geoID,
                          self.itu,
                          self.lenguajes,
                          self.independiente)


Base.metadata.create_all(engine)

