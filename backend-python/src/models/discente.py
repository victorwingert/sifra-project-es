from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from .turma_discente import TurmaDiscentes

if TYPE_CHECKING:
    from .frequencia import Frequencia
    from .turma import Turma


class Discente(SQLModel, table=True):
    __tablename__ = "discentes"  # type: ignore

    discente_id: int | None = Field(
        default=None, primary_key=True, foreign_key="usuarios.usuario_id"
    )
    matricula: str = Field(max_length=255, unique=True)
    curso: str | None = Field(default=None, max_length=255)
    semestre_ingresso: str | None = Field(default=None, max_length=20)

    turmas: list["Turma"] = Relationship(
        back_populates="discentes",
        link_model=TurmaDiscentes,
    )
    frequencias: list["Frequencia"] = Relationship(back_populates="discente")
