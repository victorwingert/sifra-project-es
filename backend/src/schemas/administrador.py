from pydantic import ConfigDict, Field, computed_field
from .usuario import UsuarioBase, UsuarioCreate, UsuarioUpdate


class AdministradorCreate(UsuarioCreate):
    pass


class AdministradorUpdate(UsuarioUpdate):
    pass


class AdministradorRead(UsuarioBase):
    usuario_id: int
    tipo_usuario: str = "ADMIN"

    model_config = ConfigDict(from_attributes=True)
