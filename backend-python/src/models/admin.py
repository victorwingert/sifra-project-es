from sqlmodel import Field, SQLModel


class Admin(SQLModel, table=True):
    __tablename__ = "administradores"  # type: ignore
    id: int | None = Field(default=None, foreign_key="usuarios.id", primary_key=True)
