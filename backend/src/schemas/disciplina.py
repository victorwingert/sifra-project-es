from pydantic import BaseModel


class DisciplinaSchema(BaseModel):
    id: int
    codigo: str
    nome: str
    carga_horaria: int
    faltas_permitidas: int

    class Config:
        from_attributes = True
