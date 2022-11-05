from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Carro(Base):
    __tablename__="carro"
    marca = Column(String)
    modelo = Column(String)
    cor = Column(String)
    placa = Column(Integer, primary_key = True)