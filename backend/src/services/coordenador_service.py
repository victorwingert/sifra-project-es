from sqlmodel import Session

from ..models import Coordenador, Usuario
from ..schemas.coordenador import CoordenadorCreate, CoordenadorUpdate


class CoordenadorService:
    def create_coordenador(
        self, session: Session, data: CoordenadorCreate
    ) -> Coordenador:
        db_usuario = Usuario(
            nome=data.nome,
            email=data.email,
            senha=data.senha,
            telefone=data.telefone,
            imagem=data.imagem,
            tipo_usuario="COORDENADOR",
        )
        session.add(db_usuario)
        session.flush()
        session.refresh(db_usuario)

        db_coordenador = Coordenador(
            usuario_id=db_usuario.usuario_id,
            departamento=data.departamento,
        )
        session.add(db_coordenador)
        session.commit()
        session.refresh(db_coordenador)
        return db_coordenador

    def update_coordenador(
        self, session: Session, usuario_id: int, data: CoordenadorUpdate
    ) -> Coordenador | None:
        db_coordenador = session.get(Coordenador, usuario_id)
        if not db_coordenador:
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

        coordenador_data = data.model_dump(exclude_unset=True)
        if "departamento" in coordenador_data:
            db_coordenador.departamento = coordenador_data["departamento"]

        session.add(db_coordenador)
        session.commit()
        session.refresh(db_coordenador)
        return db_coordenador
