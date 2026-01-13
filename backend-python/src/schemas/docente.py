from .usuario import UsuarioBase, UsuarioCreate, UsuarioUpdate


class DocenteCreate(UsuarioCreate):
    departamento: str


class DocenteUpdate(UsuarioUpdate):
    departamento: str | None = None


class DocenteRead(UsuarioBase):
    id: int
    departamento: str | None = None
    tipo_usuario: str

    class Config:
        from_attributes = True
