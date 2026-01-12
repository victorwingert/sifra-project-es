from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    senha: str


class LoginResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str | None = None
    image: str | None = None
    perfil: str
