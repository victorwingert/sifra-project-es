from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ....db.session import get_session
from ....models import Usuario
from ....services.usuario_service import UsuarioService
from ..deps import get_current_user

router = APIRouter()
service = UsuarioService()


@router.get("/me", response_model=Usuario)
def read_user_me(current_user: Usuario = Depends(get_current_user)) -> Usuario:
    return current_user


@router.get("/", response_model=list[Usuario])
def get_usuarios(
    session: Session = Depends(get_session),
) -> list[Usuario]:
    return service.list_usuarios(session)


@router.get("/{usuario_id}", response_model=Usuario)
def get_usuario(
    usuario_id: int,
    session: Session = Depends(get_session),
) -> Usuario:
    usuario = service.get_usuario(session, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario
