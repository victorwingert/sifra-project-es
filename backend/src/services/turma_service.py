from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from ..models import Discente, Turma


class TurmaService:
    def list_turmas(self, session: Session) -> list[Turma]:
        statement = select(Turma).options(selectinload(Turma.disciplina)) # type: ignore
        return list(session.exec(statement).all())

    def get_discentes(self, session: Session, turma_id: int) -> list[Discente] | None:
        turma = session.exec(
            select(Turma)
            .where(Turma.turma_id == turma_id)
            .options(
                selectinload(Turma.discentes).selectinload(Discente.usuario)  # type: ignore[arg-type]
            )
        ).first()

        return turma.discentes if turma else None
