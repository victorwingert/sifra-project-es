from sqlmodel import Field, SQLModel


class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"  # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=255, nullable=False)
    email: str = Field(max_length=255, unique=True, nullable=False)
    senha: str = Field(max_length=255, nullable=False)
    telefone: str | None = Field(default=None, max_length=255)
    image: str | None = Field(default=None, max_length=255)
    perfil: str = Field(max_length=50, nullable=False)
