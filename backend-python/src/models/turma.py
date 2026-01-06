from sqlmodel import Field, SQLModel


class Turma(SQLModel, table=True):
    __tablename__ = "turmas"  # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    ano: int = Field(nullable=False)
    semestre: str = Field(max_length=20, nullable=False)
    disciplina_id: int = Field(foreign_key="disciplinas.id", nullable=False)
    docente_id: int = Field(foreign_key="docentes.id", nullable=False)
