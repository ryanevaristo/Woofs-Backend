from fastapi import FastAPI
from sqlalchemy import Boolean, Column, DateTime, Integer, ForeignKey, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from base import Base
from models.Usuario import Usuario

class Animal(Base):
    __tablename__ = 'Animal'
    schema='dbo'

    id = Column(Integer, primary_key =True, autoincrement=True, index=True)
    nome = Column(String(50), nullable=False)
    especie = Column(String(100), nullable =False)
    sexo = Column(String(1), nullable=False)
    raca = Column(String(30), nullable=False)
    idade = Column(String(2), nullable=False)
    vacinacao = Column(String(200))
    validacao_vacina = Column(Boolean)
    id_usuario = Column(Integer, ForeignKey('Usuario.id'))
    #id_usuario = Column(String, ForeignKey('Usuario.nome'))
    usuario = relationship("Usuario")
    
    def __repr__(self) -> str:
        return super().__repr__(f"id={self.id}, nome={self.nome}, especie={self.especie} sexo={self.sexo}, idade={self.idade}, vacinacao={self.vacinacao}, validacao_vacinacao={self.vacinacao}, id_usuario={self.id_usuario}")