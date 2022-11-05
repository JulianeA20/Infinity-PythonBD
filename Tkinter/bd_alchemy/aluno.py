from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Aluno(Base):
    __tablename__="alunos"
    id = Column(Integer,primary_key = True)
    nome = Column(String)
        
