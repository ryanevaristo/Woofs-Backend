import uvicorn

from fastapi import FastAPI
#from fastapi_sqlalchemy import DBSessionMiddleware, db
from Animal import Animal as ModelAnimal
from AnimalSchema import Animal as SchemaAnimal

import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

#app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
def read_root():
    return {"User": "Teste"}

@app.get("/item/{id}}")
def read_user(id:int, q: bool | None = None):
    return {"id": id, "q": q}

@app.get("/user/")
def read_user(id:int = 0):
    if(id == 0):
        return {"users": []}
    return {"id": id}

@app.post("/animal/", response_model=SchemaAnimal)
def create_animal(animal: SchemaAnimal):
    db_animal = ModelAnimal(nome=animal.nome, sexo=animal.sexo, raca=animal.raca, idade=animal.idade, vacinacao=animal.vacinacao, validacao_vacina=animal.validacao_vacina)
