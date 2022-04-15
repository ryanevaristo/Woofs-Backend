from pydantic import BaseModel, ValidationError, validator
from typing import Optional

class AnimalID(BaseModel):
    id:int
    nome: str
    sexo: str
    raca: str
    idade: str
    vacinacao: str = None
    validacao_vacina: bool = None
    id_usuario: int

    class Config:
        orm_mode = True
class Animal(BaseModel):
    nome: str
    especie: str
    sexo: str
    raca: str
    idade: str
    vacinacao: str = None
    validacao_vacina: bool = None
    id_usuario: int

    class Config:
        orm_mode = True