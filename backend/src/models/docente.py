from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .turma import Turma
    from .usuario import Usuario


class Docente(SQLModel, table=True):
    __tablename__ = "docentes"  # type: ignore

    usuario_id: int | None = Field(
        default=None,
        primary_key=True,
        foreign_key="usuarios.usuario_id",
        ondelete="CASCADE",
    )
    departamento: str = Field(max_length=100)

    turmas: list["Turma"] = Relationship(back_populates="docente")
    usuario: "Usuario" = Relationship()
