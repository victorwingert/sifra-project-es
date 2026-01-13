from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ....db.session import get_session
from ....models import Administrador, Usuario
from ....schemas.administrador import (
    AdministradorCreate,
    AdministradorRead,
    AdministradorUpdate,
)
from ....services.administrador_service import AdministradorService
from ....services.usuario_service import UsuarioService
from ..deps import get_current_admin

router = APIRouter()
service = AdministradorService()
usuario_service = UsuarioService()


@router.post("/", response_model=AdministradorRead)
def create_administrador(
    data: AdministradorCreate,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> Administrador:
    return service.create_administrador(session, data)


@router.patch("/{usuario_id}", response_model=AdministradorRead)
def update_administrador(
    usuario_id: int,
    data: AdministradorUpdate,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> Administrador:
    updated = service.update_administrador(session, usuario_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Administrador não encontrado")
    return updated


@router.delete("/{usuario_id}")
def delete_administrador(
    usuario_id: int,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> dict[str, str]:
    admin = session.get(Administrador, usuario_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador não encontrado")

    success = usuario_service.delete_usuario(session, usuario_id)
    if not success:
        raise HTTPException(status_code=404, detail="Erro ao deletar administrador")
    return {"status": "success"}
