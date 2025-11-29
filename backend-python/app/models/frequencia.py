from sqlmodel import Field, SQLModel

class Frequencia(SQLModel, table=True):
    __tablename__ = "frequencias"

    id: int | None = Field(default=None, primary_key=True)
    presente: bool = Field(default=False, nullable=False)
    aula_id: int = Field(foreign_key="aulas.id", nullable=False)
    discente_id: int = Field(foreign_key="discentes.id", nullable=False)
