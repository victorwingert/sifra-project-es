from pydantic import BaseModel, EmailStr


class UsuarioUpdate(BaseModel):
    nome: str | None = None
    sobrenome: str | None = None
    email: EmailStr | None = None
