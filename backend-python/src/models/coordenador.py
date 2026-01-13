from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .usuario import Usuario


class Coordenador(SQLModel, table=True):
    __tablename__ = "coordenadores"  # type: ignore

    usuario_id: int | None = Field(
        default=None,
        primary_key=True,
        foreign_key="usuarios.usuario_id",
        ondelete="CASCADE",
    )
    departamento: str | None = Field(default=None, max_length=255)

    usuario: "Usuario" = Relationship()
