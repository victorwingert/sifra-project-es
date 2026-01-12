from sqlmodel import Session, select

from ..models import Coordenador, Discente, Docente, Usuario
from ..schemas.usuario import UsuarioUpdate


class UsuarioService:
    def get_usuario(self, session: Session, usuario_id: int) -> Usuario | None:
        return session.get(Usuario, usuario_id)

    def list_usuarios(self, session: Session) -> list[Usuario]:
        statement = select(Usuario)
        return list(session.exec(statement).all())

    def create_docente(self, session: Session, data: Docente) -> None:
        session.add(data)
        session.commit()

    def create_discente(self, session: Session, data: Discente) -> None:
        session.add(data)
        session.commit()

    def create_coordenador(self, session: Session, data: Coordenador) -> None:
        session.add(data)
        session.commit()

    def delete_usuario(self, session: Session, usuario_id: int) -> bool:
        usuario = session.get(Usuario, usuario_id)

        if not usuario:
            return False

        session.delete(usuario)
        session.commit()
        return True

    def update_usuario(
        self, session: Session, usuario_id: int, data: UsuarioUpdate
    ) -> Usuario | None:
        db_usuario = session.get(Usuario, usuario_id)
        if not db_usuario:
            return None
        usuario_data = data.model_dump(exclude_unset=True)
        db_usuario.sqlmodel_update(usuario_data)
        session.add(db_usuario)
        session.commit()
        session.refresh(db_usuario)
        return db_usuario
