from .usuario import UsuarioBase, UsuarioCreate, UsuarioUpdate


class CoordenadorCreate(UsuarioCreate):
    departamento: str


class CoordenadorUpdate(UsuarioUpdate):
    departamento: str | None = None


class CoordenadorRead(UsuarioBase):
    id: int
    departamento: str | None = None
    tipo_usuario: str

    class Config:
        from_attributes = True
