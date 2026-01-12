from datetime import UTC, datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .frequencia import Frequencia
    from .turma import Turma


class Aula(SQLModel, table=True):
    __tablename__ = "aulas"  # type: ignore

    aula_id: int | None = Field(default=None, primary_key=True)
    data: datetime = Field(default_factory=lambda: datetime.now(UTC))
    conteudo: str | None = Field(default=None)

    turma_id: int = Field(foreign_key="turmas.turma_id")

    turma: Optional["Turma"] = Relationship(back_populates="aulas")
    frequencias: list["Frequencia"] = Relationship(back_populates="aula")
