from sqlmodel import Field, SQLModel


class TurmaDiscenteLink(SQLModel, table=True):
    __tablename__ = "turma_discentes"  # type: ignore

    turma_id: int | None = Field(
        default=None, foreign_key="turmas.id", primary_key=True
    )
    discente_id: int | None = Field(
        default=None, foreign_key="discentes.id", primary_key=True
    )
