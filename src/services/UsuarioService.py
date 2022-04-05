from typing import Optional
from sqlalchemy.orm import Session

from services.service import ServiceInterface
from models.Usuario import Usuario as ModelUsuario

class Usuario(ServiceInterface):
    def __init__(self, db: Session):
        self.db = db
    def criar(self, Usuario: ModelUsuario):
        self.db.add(Usuario)
        self.db.commit()
        self.db.refresh(Usuario)
        return Usuario

    def atualizar(self,  Usuario: ModelUsuario):
        UsuarioAtualizar = self.db.query(ModelUsuario).get(Usuario.id)
        UsuarioAtualizar.nome = Usuario.nome
        UsuarioAtualizar.email = Usuario.email
        UsuarioAtualizar.senha = Usuario.senha
        UsuarioAtualizar.idade = Usuario.idade

        self.db.commit()
        return UsuarioAtualizar
    
    def listar(self, id: Optional[int]):
        return super().listar()
    
    def remover(self, id: int):
        return super().remover()
    
   
