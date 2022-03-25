from pip import List
import uvicorn

from fastapi import FastAPI

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
#from fastapi_sqlalchemy import DBSessionMiddleware, db
from models.Animal import Animal as ModelAnimal
from schema.AnimalSchema import Animal as SchemaAnimal

from database.db import SessionLocal, engine
import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
#app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

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
def create_animal(animal: SchemaAnimal, db: Session = Depends(get_db)):
    db_animal = ModelAnimal(nome=animal.nome, sexo=animal.sexo,
                             raca=animal.raca, idade=animal.idade,
                             vacinacao=animal.vacinacao, validacao_vacina=animal.validacao_vacina)
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

@app.get("/animal/")
def get_animal(db: Session = Depends(get_db)):
    animal = db.query(ModelAnimal).all()
    return animal
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)