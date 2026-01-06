from sqlmodel import Session, select

from ..models.turma import Turma


class TurmaService:
    def list_turmas(self, session: Session) -> list[Turma]:
        return list(session.exec(select(Turma)).all())
