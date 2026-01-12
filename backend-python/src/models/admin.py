from sqlmodel import Field, SQLModel


class Administrador(SQLModel, table=True):
    __tablename__ = "administradores"  # type: ignore

    administrador_id: int | None = Field(
        default=None, primary_key=True, foreign_key="usuarios.usuario_id"
    )
