from fastapi import APIRouter, Depends
from models.Usuario import Usuario
from schema.LocalidadeSchema import Localidade as SchemaLocalidade
from models.Localidade import Localidade as ModelLocalidade
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from database import db
from services.LocalidadeService import Localidade as ServiceLocalidade


router = APIRouter()


@router.post("/animal/localidade", response_model=SchemaLocalidade)
async def Create_Localidade(Localidade: SchemaLocalidade, db: Session = Depends(db.get_db)):
    db_localidade = ModelLocalidade(longitude=Localidade.longitude,
                                    latitude=Localidade.latitude,
                                    limiteDistancia=Localidade.limiteDistanciaMatch
                                    )

    service = ServiceLocalidade(db)
    return await service.criar(db_localidade)


@router.get("/animal/localidade")
async def get_localidade(db: Session = Depends(db.get_db)):
    service = ServiceLocalidade(db)
    return await service.listar()


@router.get("/animal/localidade{id}")
async def get_localidadeId(db: Session = Depends(db.get_db)):
    service = ServiceLocalidade(db)
    return await service.listar(id)
