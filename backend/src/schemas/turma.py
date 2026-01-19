from sqlmodel import SQLModel

from ..models.disciplina import Disciplina


class TurmaRead(SQLModel):
    turma_id: int
    ano: int
    semestre: str
    disciplina: Disciplina
