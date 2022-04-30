from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.future import select
from services.service import ServiceInterface
from models.Localidade import Localidade as ModelLocalidade


class Localidade(ServiceInterface):
    def __init__(self, db: Session):
        self.db = db

    def criar(self, localidade: ModelLocalidade):
        self.db.add(localidade)
        self.db.commit()
        self.db.refresh(localidade)
        return localidade

    def atualizar(self, localidade: ModelLocalidade):
        localidadeAtualizar = self.db.query(ModelLocalidade).get(localidade.id)
        localidadeAtualizar.longitude = localidade.longitude
        localidadeAtualizar.latitude = localidade.latitude
        localidadeAtualizar.limiteDistanciaMatch = localidade.limiteDistanciaMatch

        self.db.commit()
        return localidadeAtualizar

    def listar(self, id: Optional[int]):
        return super().listar()

    def remover(self, id: int):
        return super().remover()