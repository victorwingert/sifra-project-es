from sqlmodel import Field, SQLModel

class Discente(SQLModel, table=True):
    __tablename__ = "discentes"
    id: int | None = Field(default=None, foreign_key="usuarios.id", primary_key=True)
    matricula: str = Field(max_length=255, unique=True, nullable=False)
    curso: str | None = Field(default=None, max_length=255)
    semestre_ingresso: str | None = Field(default=None, max_length=20)
