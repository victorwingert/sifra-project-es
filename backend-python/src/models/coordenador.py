from sqlmodel import Field, SQLModel


class Coordenador(SQLModel, table=True):
    __tablename__ = "coordenadores"  # type: ignore

    coordenador_id: int | None = Field(
        default=None, primary_key=True, foreign_key="usuarios.usuario_id"
    )
    departamento: str | None = Field(default=None, max_length=255)
