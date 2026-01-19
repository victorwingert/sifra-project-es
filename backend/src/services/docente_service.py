from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from ..models import Docente, Turma, Usuario
from ..schemas.docente import DocenteCreate, DocenteRead, DocenteUpdate


class DocenteService:
    def get_turmas(self, session: Session, usuario_id: int) -> list[Turma] | None:
        docente = session.get(Docente, usuario_id)
        if not docente:
            return None

        statement = (
            select(Turma)
            .where(Turma.docente_id == usuario_id)
            .options(selectinload(Turma.disciplina))  # type: ignore
        )
        return list(session.exec(statement).all())

    def create_docente(self, session: Session, data: DocenteCreate) -> DocenteRead:
        statement = select(Usuario).where(Usuario.email == data.email)
        if session.exec(statement).first():
            raise HTTPException(status_code=400, detail="E-mail já cadastrado")

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
        return DocenteRead(
            id=db_usuario.usuario_id,  # type: ignore
            nome=db_usuario.nome,
            email=db_usuario.email,
            telefone=db_usuario.telefone,
            imagem=db_usuario.imagem,
            tipo_usuario=db_usuario.tipo_usuario,
            departamento=db_docente.departamento,
            usuario_id=db_usuario.usuario_id,  # type: ignore
        )

    def update_docente(
        self, session: Session, usuario_id: int, data: DocenteUpdate
    ) -> DocenteRead | None:
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

        if db_usuario:
            return DocenteRead(
                id=db_usuario.usuario_id,  # type: ignore
                nome=db_usuario.nome,
                email=db_usuario.email,
                telefone=db_usuario.telefone,
                imagem=db_usuario.imagem,
                tipo_usuario=db_usuario.tipo_usuario,
                departamento=db_docente.departamento,
                usuario_id=db_usuario.usuario_id,  # type: ignore
            )
        return None
