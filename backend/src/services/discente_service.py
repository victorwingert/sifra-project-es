from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from ..models import Discente, Turma, TurmaDiscentes, Usuario
from ..schemas.discente import DiscenteCreate, DiscenteRead, DiscenteUpdate


class DiscenteService:
    def get_turmas(self, session: Session, usuario_id: int) -> list[Turma] | None:
        discente = session.get(Discente, usuario_id)
        if not discente:
            return None

        statement = (
            select(Turma)
            .join(TurmaDiscentes)
            .where(TurmaDiscentes.discente_id == usuario_id)
            .options(selectinload(Turma.disciplina))  # type: ignore
        )
        return list(session.exec(statement).all())

    def create_discente(self, session: Session, data: DiscenteCreate) -> DiscenteRead:
        statement = select(Usuario).where(Usuario.email == data.email)
        if session.exec(statement).first():
            raise HTTPException(status_code=400, detail="E-mail já cadastrado")

        db_usuario = Usuario(
            nome=data.nome,
            email=data.email,
            senha=data.senha,
            telefone=data.telefone,
            imagem=data.imagem,
            tipo_usuario="DISCENTE",
        )
        session.add(db_usuario)
        session.flush()
        session.refresh(db_usuario)

        db_discente = Discente(
            usuario_id=db_usuario.usuario_id,
            matricula=data.matricula,
            curso=data.curso,
            semestre_ingresso=data.semestre_ingresso,
        )
        session.add(db_discente)
        session.commit()
        session.refresh(db_discente)
        
        return DiscenteRead(
            id=db_usuario.usuario_id,  # type: ignore
            nome=db_usuario.nome,
            email=db_usuario.email,
            telefone=db_usuario.telefone,
            imagem=db_usuario.imagem,
            tipo_usuario=db_usuario.tipo_usuario,
            matricula=db_discente.matricula,
            curso=db_discente.curso,
            semestre_ingresso=db_discente.semestre_ingresso,
        )

    def update_discente(
        self, session: Session, usuario_id: int, data: DiscenteUpdate
    ) -> DiscenteRead | None:
        db_discente = session.get(Discente, usuario_id)
        if not db_discente:
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

        discente_data = data.model_dump(exclude_unset=True)
        if "matricula" in discente_data:
            db_discente.matricula = discente_data["matricula"]
        if "curso" in discente_data:
            db_discente.curso = discente_data["curso"]
        if "semestre_ingresso" in discente_data:
            db_discente.semestre_ingresso = discente_data["semestre_ingresso"]

        session.add(db_discente)
        session.commit()
        session.refresh(db_discente)
        
        if db_usuario:
            return DiscenteRead(
                id=db_usuario.usuario_id,  # type: ignore
                nome=db_usuario.nome,
                email=db_usuario.email,
                telefone=db_usuario.telefone,
                imagem=db_usuario.imagem,
                tipo_usuario=db_usuario.tipo_usuario,
                matricula=db_discente.matricula,
                curso=db_discente.curso,
                semestre_ingresso=db_discente.semestre_ingresso,
            )
        return None
