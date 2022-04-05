from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.future import select
#from service import ServiceInterface
from models.Animal import Animal as ModelAnimal

class Animal():
    def __init__(self, db: Session):
        self.db = db
    async def criar(self, animal: ModelAnimal):
        self.db.add(animal)
        await self.db.flush()

    async def atualizar(self,  animal: ModelAnimal):
        animalAtualizar = self.db.query(ModelAnimal).get(animal.id)
        animalAtualizar.nome = animal.nome
        animalAtualizar.raca = animal.raca
        animalAtualizar.sexo = animal.sexo
        animalAtualizar.idade = animal.idade
        animalAtualizar.vacinacao = animal.vacinacao
        animalAtualizar.validacao_vacina = animal.validacao_vacina
        await self.db.commit()
        return animalAtualizar
    
    async def listar(self, id: Optional[int]):
        return super().listar()
    
    async def remover(self, id: int):
        return super().remover()
    
   
