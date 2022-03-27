from typing import Optional
from sqlalchemy.orm import Session

#from service import ServiceInterface
from models.Animal import Animal as ModelAnimal

class Animal():
    def __init__(self, db: Session):
        self.db = db
    def criar(self, animal: ModelAnimal):
        self.db.add(animal)
        self.db.commit()
        self.db.refresh(animal)
        return animal

    def atualizar(self,  animal: ModelAnimal):
        animalAtualizar = self.db.query(ModelAnimal).get(animal.id)
        animalAtualizar.nome = animal.nome
        animalAtualizar.raca = animal.raca
        animalAtualizar.sexo = animal.sexo
        animalAtualizar.idade = animal.idade
        animalAtualizar.vacinacao = animal.vacinacao
        animalAtualizar.validacao_vacina = animal.validacao_vacina

        self.db.commit()
        return animalAtualizar
    
    def listar(self, id: Optional[int]):
        return super().listar()
    
    def remover(self, id: int):
        return super().remover()
    
   
