from pickle import TRUE
import string
from tokenize import String
from pydantic import BaseModel, ValidationError, validator

class Animal(BaseModel):
    id: int
    nome: string
    sexo: string
    raca: string
    idade: string
    vacinacao: string = None
    validacao_vacina: bool
    ##id_usuario = int

    class Config:
        orm_mode = True