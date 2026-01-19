from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from ..models import Turma, Discente


class TurmaService:
    def list_turmas(self, session: Session) -> list[Turma]:
        return list(session.exec(select(Turma)).all())

    def get_discentes(self, session: Session, turma_id: int) -> list[Discente] | None:
        turma = session.exec(
            select(Turma)
            .where(Turma.turma_id == turma_id)
            .options(selectinload(Turma.discentes).selectinload(Discente.usuario))
        ).first()
        
        return turma.discentes if turma else None
