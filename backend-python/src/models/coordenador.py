from sqlmodel import Field, SQLModel


class Coordenador(SQLModel, table=True):
    __tablename__ = "coordenadores"  # type: ignore

    id: int | None = Field(default=None, foreign_key="usuarios.id", primary_key=True)
    departamento: str | None = Field(default=None, max_length=255)
