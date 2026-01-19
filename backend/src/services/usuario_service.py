from sqlmodel import Session, select

from ..models import Usuario


class UsuarioService:
    def get_usuario(self, session: Session, usuario_id: int) -> Usuario | None:
        return session.get(Usuario, usuario_id)

    def list_usuarios(self, session: Session) -> list[Usuario]:
        statement = select(Usuario)
        return list(session.exec(statement).all())

    def delete_usuario(self, session: Session, usuario_id: int) -> bool:
        usuario = session.get(Usuario, usuario_id)
        if not usuario:
            return False
        session.delete(usuario)
        session.commit()
        return True
