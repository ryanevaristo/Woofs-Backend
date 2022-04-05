from fastapi import APIRouter, Depends
from models.Usuario import Usuario
from schema.AnimalSchema import Animal as SchemaAnimal
from models.Animal import Animal as ModelAnimal
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from services.AnimalService import Animal as ServiceAnimal

router = APIRouter()

@router.post("/animal/", response_model=SchemaAnimal)
async def create_animal(animal: SchemaAnimal, dbSession: AsyncSession = Depends(get_db)):
        db_animal = ModelAnimal(nome=animal.nome, sexo=animal.sexo,
                        raca=animal.raca, idade=animal.idade,
                        vacinacao=animal.vacinacao,
                        validacao_vacina=animal.validacao_vacina,
                        id_usuario=animal.id_usuario
                    )
        service = ServiceAnimal(dbSession)
        return await service.criar(db_animal)
    

@router.get("/animal/")
async def get_animal(dbSession: AsyncSession = Depends(get_db)):
    service = ServiceAnimal(dbSession)
    return await service.listar()
    #animal = db.query(ModelAnimal).all()
    #return animal


@router.get("/animal/{id}")
async def get_animalId(id: int, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceAnimal(dbSession)
    return await service.listar(id)
