from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .aula import Aula
    from .discente import Discente


class Frequencia(SQLModel, table=True):
    __tablename__ = "frequencias"  # type: ignore

    frequencia_id: int | None = Field(default=None, primary_key=True)
    presente: bool = False

    aula_id: int = Field(foreign_key="aulas.aula_id")
    discente_id: int = Field(foreign_key="discentes.usuario_id")

    aula: Optional["Aula"] = Relationship(back_populates="frequencias")
    discente: Optional["Discente"] = Relationship(back_populates="frequencias")
