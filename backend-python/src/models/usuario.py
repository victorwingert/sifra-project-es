from sqlmodel import Field, SQLModel


class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"  # type: ignore

    usuario_id: int | None = Field(default=None, primary_key=True)
    nome: str
    email: str = Field(unique=True)
    senha: str
    telefone: str | None = None
    image: str | None = None
    perfil: str
