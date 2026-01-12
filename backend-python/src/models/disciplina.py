from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .turma import Turma


class Disciplina(SQLModel, table=True):
    __tablename__ = "disciplinas"  # type: ignore

    disciplina_id: int | None = Field(default=None, primary_key=True)
    codigo: str = Field(max_length=50)
    nome: str = Field(max_length=255)
    carga_horaria: int
    faltas_permitidas: int

    turmas: list["Turma"] = Relationship(back_populates="disciplina")
