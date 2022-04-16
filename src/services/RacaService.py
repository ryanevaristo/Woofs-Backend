from typing import Optional
from sqlalchemy.orm  import Session
from sqlalchemy import update, delete
from sqlalchemy.future import select

from .service import ServiceInterface
from models.Raca import Raca as ModelRaca
from schema.RacaSchema import Raca as SchemaRaca

class Raca(ServiceInterface):
    def __init__(self, db: Session) -> None:
        self.db = db
    
    async def criar(self, raca: SchemaRaca):
        db_raca = ModelRaca(
            nome=raca.nome
        )
        self.db.add(db_raca)
        await self.db.flush()
    
    async def atualizar(self, raca: SchemaRaca, id: int):
        db_raca = (
            update(ModelRaca)
            .where(ModelRaca.id == id)
            .values(**raca.dict())
            .execution_options(synchronize_session="fetch")
        )
        await self.db.execute(db_raca)
        return raca.dict()

    async def remover(self, id: int):
        query = delete(ModelRaca).where(ModelRaca.id == id)
        await self.db.execute(query)
    
    async def listar(self, id: Optional[int]):
        if id:
            query = select(ModelRaca).where(ModelRaca.id == id)
            resultados = await self.db.execute(query)
            (resultado, ) = resultados.one()
            return resultado
        else:
            query = select(ModelRaca)
            resultados = await self.db.execute(query)
            return resultados.scalars().all()