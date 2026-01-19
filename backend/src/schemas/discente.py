from pydantic import BaseModel

from .usuario import UsuarioBase, UsuarioCreate, UsuarioRead, UsuarioUpdate


class DiscenteCreate(UsuarioCreate):
    matricula: str
    curso: str
    semestre_ingresso: str


class DiscenteUpdate(UsuarioUpdate):
    matricula: str | None = None
    curso: str | None = None
    semestre_ingresso: str | None = None


class DiscenteRead(UsuarioBase):
    id: int
    matricula: str
    curso: str | None = None
    semestre_ingresso: str | None = None
    tipo_usuario: str
    faltas: int | None = None

    class Config:
        from_attributes = True


class DiscenteComUsuario(BaseModel):
    usuario: UsuarioRead
    matricula: str
    curso: str | None
    semestre_ingresso: str | None

    class Config:
        from_attributes = True
