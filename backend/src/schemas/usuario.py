from pydantic import BaseModel, ConfigDict, EmailStr


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: str | None = None
    imagem: str | None = None


class UsuarioCreate(UsuarioBase):
    senha: str


class UsuarioUpdate(BaseModel):
    nome: str | None = None
    sobrenome: str | None = None
    email: EmailStr | None = None
    telefone: str | None = None
    imagem: str | None = None


class UsuarioRead(UsuarioBase):
    usuario_id: int
    tipo_usuario: str

    model_config = ConfigDict(from_attributes=True)
