from sqlmodel import Field, SQLModel


class TurmaDiscentes(SQLModel, table=True):
    __tablename__ = "turma_discentes"  # type: ignore

    turma_id: int | None = Field(
        default=None, foreign_key="turmas.turma_id", primary_key=True
    )
    discente_id: int | None = Field(
        default=None, foreign_key="discentes.discente_id", primary_key=True
    )
