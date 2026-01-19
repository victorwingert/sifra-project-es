from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

from .turma_discente import TurmaDiscentes

if TYPE_CHECKING:
    from .aula import Aula
    from .discente import Discente
    from .disciplina import Disciplina
    from .docente import Docente


class Turma(SQLModel, table=True):
    __tablename__ = "turmas"  # type: ignore

    turma_id: int | None = Field(default=None, primary_key=True)
    ano: int
    semestre: str = Field(max_length=20)

    disciplina_id: int = Field(foreign_key="disciplinas.disciplina_id")
    docente_id: int = Field(foreign_key="docentes.usuario_id")

    disciplina: Optional["Disciplina"] = Relationship(back_populates="turmas")
    docente: Optional["Docente"] = Relationship(back_populates="turmas")
    aulas: list["Aula"] = Relationship(back_populates="turma")
    discentes: list["Discente"] = Relationship(
        back_populates="turmas", link_model=TurmaDiscentes
    )
