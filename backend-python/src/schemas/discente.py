from pydantic import BaseModel


class DiscenteSchema(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str | None = None
    image: str | None = None
    matricula: str
    curso: str | None = None
    semestre_ingresso: str | None = None
    perfil: str
    faltas: int

    class Config:
        from_attributes = True
