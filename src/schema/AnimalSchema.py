from pydantic import BaseModel, ValidationError, validator
from typing import Optional

class Animal(BaseModel):
    nome: str
    sexo: str
    raca: str
    idade: str
    vacinacao: str = None
    validacao_vacina: bool = None
    id_usuario: int

    class Config:
        orm_mode = True