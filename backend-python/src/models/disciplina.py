from sqlmodel import Field, SQLModel


class Disciplina(SQLModel, table=True):
    __tablename__ = "disciplinas"  # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    codigo: str = Field(max_length=50, nullable=False)
    nome: str = Field(max_length=255, nullable=False)
    carga_horaria: int = Field(nullable=False)
    faltas_permitidas: int = Field(nullable=False)
