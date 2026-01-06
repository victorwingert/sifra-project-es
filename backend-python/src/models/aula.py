from datetime import datetime

from sqlmodel import Field, SQLModel


class Aula(SQLModel, table=True):
    __tablename__ = "aulas"  # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    data: datetime = Field(default_factory=datetime.now, nullable=False)
    conteudo: str | None = Field(default=None)
    turma_id: int = Field(foreign_key="turmas.id", nullable=False)
