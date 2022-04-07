from typing import Optional
from fastapi import Query
from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from sqlalchemy.future import select
#from service import ServiceInterface
from models.Animal import Animal as ModelAnimal
from schema.AnimalSchema import Animal as SchemaAnimal
class Animal():
    def __init__(self, db: Session):
        self.db = db
    async def criar(self, animal: ModelAnimal):
        self.db.add(animal)
        await self.db.flush()

    async def atualizar(self,  animal: SchemaAnimal, id: int):
        animalAtualizar = (
            update(ModelAnimal)
            .where(ModelAnimal.id == id)
            .values(**animal.dict())
            .execution_options(synchronize_session="fetch")
        )
        #.values(nome = animal.nome).execution_options(synchronize_session="fetch")
        print(animalAtualizar)
        await self.db.execute(animalAtualizar)

        return animal.dict()
    
    async def listar(self, id: Optional[int]):
        if(id):
            query = select(ModelAnimal).where(ModelAnimal.id == id)
            resultados = await self.db.execute(query)
            (resulto, ) = resultados.one()
            return resulto
        else:
            query = select(ModelAnimal)
            resultados = await self.db.execute(query)
            return resultados.scalars().all()
    
    async def remover(self, id: int):
        query = delete(ModelAnimal).where(ModelAnimal.id == id)
        await self.db.execute(query)

    
   
