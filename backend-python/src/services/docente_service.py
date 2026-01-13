from sqlmodel import Session

from ..models import Docente, Turma, Usuario
from ..schemas.docente import DocenteCreate, DocenteUpdate


class DocenteService:
    def get_turmas(self, session: Session, usuario_id: int) -> list[Turma] | None:
        docente = session.get(Docente, usuario_id)
        if not docente:
            return None
        return docente.turmas

    def create_docente(self, session: Session, data: DocenteCreate) -> Docente:
        db_usuario = Usuario(
            nome=data.nome,
            email=data.email,
            senha=data.senha,
            telefone=data.telefone,
            imagem=data.imagem,
            tipo_usuario="DOCENTE",
        )
        session.add(db_usuario)
        session.flush()
        session.refresh(db_usuario)

        db_docente = Docente(
            usuario_id=db_usuario.usuario_id,
            departamento=data.departamento,
        )
        session.add(db_docente)
        session.commit()
        session.refresh(db_docente)
        return db_docente

    def update_docente(
        self, session: Session, usuario_id: int, data: DocenteUpdate
    ) -> Docente | None:
        db_docente = session.get(Docente, usuario_id)
        if not db_docente:
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

        docente_data = data.model_dump(exclude_unset=True)
        if "departamento" in docente_data:
            db_docente.departamento = docente_data["departamento"]

        session.add(db_docente)
        session.commit()
        session.refresh(db_docente)
        return db_docente
