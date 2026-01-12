from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .turma import Turma


class Docente(SQLModel, table=True):
    __tablename__ = "docentes"  # type: ignore

    docente_id: int | None = Field(
        default=None, primary_key=True, foreign_key="usuarios.usuario_id"
    )
    departamento: str | None = Field(default=None, max_length=255)

    turmas: list["Turma"] = Relationship(back_populates="docente")
