from sqlmodel import Session

from ..models import Administrador, Usuario
from ..schemas.administrador import AdministradorCreate, AdministradorUpdate


class AdministradorService:
    def create_administrador(
        self, session: Session, data: AdministradorCreate
    ) -> Administrador:
        db_usuario = Usuario(
            nome=data.nome,
            email=data.email,
            senha=data.senha,
            telefone=data.telefone,
            imagem=data.imagem,
            tipo_usuario="ADMIN",
        )
        session.add(db_usuario)
        session.flush()
        session.refresh(db_usuario)

        db_admin = Administrador(usuario_id=db_usuario.usuario_id)
        session.add(db_admin)
        session.commit()
        session.refresh(db_admin)
        return db_admin

    def update_administrador(
        self, session: Session, usuario_id: int, data: AdministradorUpdate
    ) -> Administrador | None:
        db_admin = session.get(Administrador, usuario_id)
        if not db_admin:
            return None

        db_usuario = session.get(Usuario, usuario_id)
        if db_usuario:
            usuario_data = data.model_dump(exclude_unset=True)
            base_data = {
                k: v
                for k, v in usuario_data.items()
                if k in ["nome", "sobrenome", "email", "telefone", "imagem"]
            }
            db_usuario.sqlmodel_update(base_data)
            session.add(db_usuario)

        session.add(db_admin)
        session.commit()
        session.refresh(db_admin)
        return db_admin
