from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    email: str
    senha: str
    idade: str
    id_localidade: int

    class Config:
        orm_mode = True