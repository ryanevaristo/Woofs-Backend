from fastapi import APIRouter, Depends
from schema.UsuarioSchema import Usuario as SchemaUsuario
from models.Usuario import Usuario as ModelUsuario
from sqlalchemy.orm import Session
from database import db
from services.UsuarioService import Usuario as ServiceUsuario

router = APIRouter()

@router.post("/user/", response_model=SchemaUsuario)
async def create_usuario(usuario: SchemaUsuario, db: Session = Depends(db.get_db)):
    db_usuario =  ModelUsuario(nome=usuario.nome,
                             email=usuario.email, 
                             idade=usuario.idade,
                             senha=usuario.senha,
                             fk_localidade=usuario.id_localidade
                             )
    service = ServiceUsuario(db)
    return service.criar(db_usuario)
    

@router.get("/usuario/")
def get_usuario(db: Session = Depends(db.get_db)):
    service = ServiceUsuario(db)
    return service.listar()
    #usuario = db.query(ModelUsuario).all()
    #return usuario


@router.get("/usuario/{id}")
def get_usuarioId(id: int, db: Session = Depends(db.get_db)):
    service = ServiceUsuario(db)
    return service.listar(id)
