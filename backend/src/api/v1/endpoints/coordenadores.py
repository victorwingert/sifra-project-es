from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ....db.session import get_session
from ....models import Coordenador, Usuario
from ....schemas.coordenador import (
    CoordenadorCreate,
    CoordenadorRead,
    CoordenadorUpdate,
)
from ....services.coordenador_service import CoordenadorService
from ....services.usuario_service import UsuarioService
from ..deps import get_current_admin

router = APIRouter()
service = CoordenadorService()
usuario_service = UsuarioService()


@router.post("/", response_model=CoordenadorRead)
def create_coordenador(
    data: CoordenadorCreate,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> CoordenadorRead:
    return service.create_coordenador(session, data)


@router.patch("/{usuario_id}", response_model=CoordenadorRead)
def update_coordenador(
    usuario_id: int,
    data: CoordenadorUpdate,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> CoordenadorRead:
    updated = service.update_coordenador(session, usuario_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Coordenador não encontrado")
    return updated


@router.delete("/{usuario_id}")
def delete_coordenador(
    usuario_id: int,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> dict[str, str]:
    coordenador = session.get(Coordenador, usuario_id)
    if not coordenador:
        raise HTTPException(status_code=404, detail="Coordenador não encontrado")

    success = usuario_service.delete_usuario(session, usuario_id)
    if not success:
        raise HTTPException(status_code=404, detail="Erro ao deletar coordenador")
    return {"status": "success"}
