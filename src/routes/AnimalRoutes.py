from typing import Optional
from fastapi import APIRouter, Depends
from models.Usuario import Usuario
from schema.AnimalSchema import Animal as SchemaAnimal
from schema.AnimalSchema import AnimalID as SchemaAnimalId
from models.Animal import Animal as ModelAnimal
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from services.AnimalService import Animal as ServiceAnimal

router = APIRouter()

@router.post("/animal/", response_model=SchemaAnimal)
async def create_animal(animal: SchemaAnimal, dbSession: AsyncSession = Depends(get_db)):
        service = ServiceAnimal(dbSession)
        return await service.criar(animal)
    
@router.put("/animal/{id}", response_model=SchemaAnimal)
async def get_animal(id: int, animal: SchemaAnimal, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceAnimal(dbSession)
    return await service.atualizar(animal, id)

@router.get("/animal/")
async def get_animalId(id: Optional[int] = None, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceAnimal(dbSession)
    return await service.listar(id)
    
@router.delete("/animal/{id}")
async def delete_animal(id: int, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceAnimal(dbSession)
    return await service.remover(id)
