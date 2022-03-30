from fastapi import APIRouter, Depends
from models.Usuario import Usuario
from schema.AnimalSchema import Animal as SchemaAnimal
from models.Animal import Animal as ModelAnimal
from sqlalchemy.orm import Session
from database import db
from services.AnimalService import Animal as ServiceAnimal
import asyncio

router = APIRouter()

@router.post("/animal/", response_model=SchemaAnimal)
async def create_animal(animal: SchemaAnimal, db: Session = Depends(db.get_db)):
    db_animal =  ModelAnimal(nome=animal.nome, sexo=animal.sexo,
                             raca=animal.raca, idade=animal.idade,
                             vacinacao=animal.vacinacao,
                             validacao_vacina=animal.validacao_vacina,
                             id_usuario=animal.id_usuario
                             )
    service = ServiceAnimal(db)
    return service.criar(db_animal)
    

@router.get("/animal/")
def get_animal(db: Session = Depends(db.get_db)):
    service = ServiceAnimal(db)
    return service.listar()
    #animal = db.query(ModelAnimal).all()
    #return animal


@router.get("/animal/{id}")
def get_animalId(id: int, db: Session = Depends(db.get_db)):
    service = ServiceAnimal(db)
    return service.listar(id)
