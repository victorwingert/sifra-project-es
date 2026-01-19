from pydantic import ConfigDict

from .usuario import UsuarioBase, UsuarioCreate, UsuarioUpdate


class DocenteCreate(UsuarioCreate):
    departamento: str


class DocenteUpdate(UsuarioUpdate):
    departamento: str | None = None


class DocenteRead(UsuarioBase):
    id: int
    departamento: str | None = None
    tipo_usuario: str

    model_config = ConfigDict(from_attributes=True)
