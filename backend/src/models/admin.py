from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .usuario import Usuario


class Administrador(SQLModel, table=True):
    __tablename__ = "administradores"  # type: ignore

    usuario_id: int | None = Field(
        default=None,
        primary_key=True,
        foreign_key="usuarios.usuario_id",
        ondelete="CASCADE",
    )

    usuario: "Usuario" = Relationship()
