from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ....db.session import get_session
from ....models import Discente, Turma, Usuario
from ....schemas.discente import DiscenteCreate, DiscenteRead, DiscenteUpdate
from ....services.discente_service import DiscenteService
from ....services.usuario_service import UsuarioService
from ..deps import get_current_admin, get_current_coordenador, get_current_user

router = APIRouter()
service = DiscenteService()
usuario_service = UsuarioService()


@router.get("/{usuario_id}/turmas", response_model=list[Turma])
def get_discente_turmas(
    usuario_id: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_user),
) -> list[Turma]:
    if current_user.usuario_id != usuario_id:
        get_current_coordenador(current_user)

    turmas = service.get_turmas(session, usuario_id)
    if turmas is None:
        raise HTTPException(status_code=404, detail="Discente informado não existe")
    return turmas


@router.post("/", response_model=DiscenteRead)
def create_discente(
    data: DiscenteCreate,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> Discente:
    return service.create_discente(session, data)


@router.patch("/{usuario_id}", response_model=DiscenteRead)
def update_discente(
    usuario_id: int,
    data: DiscenteUpdate,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> Discente:
    updated = service.update_discente(session, usuario_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Discente não encontrado")
    return updated


@router.delete("/{usuario_id}")
def delete_discente(
    usuario_id: int,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> dict[str, str]:
    discente = session.get(Discente, usuario_id)
    if not discente:
        raise HTTPException(status_code=404, detail="Discente não encontrado")

    success = usuario_service.delete_usuario(session, usuario_id)
    if not success:
        raise HTTPException(status_code=404, detail="Erro ao deletar discente")
    return {"status": "success"}
