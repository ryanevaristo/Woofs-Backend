from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import get_db
from schema.RacaSchema import Raca as SchemaRaca
from models.Raca import Raca as ModelRaca
from services.RacaService import Raca as ServiceRaca

router = APIRouter()

@router.post("/raca/", response_model=SchemaRaca)
async def criar_raca(raca: SchemaRaca, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceRaca(dbSession)
    return await service.criar(raca)

@router.put("/raca/{id}", response_model=SchemaRaca)
async def atualizar_raca(id: int, raca: SchemaRaca, dbSession: AsyncSession = Depends(get_db)):
    service =  ServiceRaca(dbSession)
    return await service.atualizar(raca=raca, id=id)

@router.get("/raca/")
async def get_raca(id: Optional[int] = None, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceRaca(dbSession)
    return await service.listar(id)

@router.delete("/raca/{id}")
async def delete_raca(id: int, dbSession: AsyncSession = Depends(get_db)):
    service = ServiceRaca(dbSession)
    return await service.remover(id)