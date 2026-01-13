from .usuario import UsuarioBase, UsuarioCreate, UsuarioUpdate


class AdministradorCreate(UsuarioCreate):
    pass


class AdministradorUpdate(UsuarioUpdate):
    pass


class AdministradorRead(UsuarioBase):
    id: int
    tipo_usuario: str

    class Config:
        from_attributes = True
