from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ....db.session import get_session
from ....models import Docente, Turma, Usuario
from ....schemas.docente import DocenteCreate, DocenteRead, DocenteUpdate
from ....schemas.turma import TurmaRead
from ....services.docente_service import DocenteService
from ....services.usuario_service import UsuarioService
from ..deps import get_current_admin, get_current_coordenador, get_current_user

router = APIRouter()
service = DocenteService()
usuario_service = UsuarioService()


@router.get("/{usuario_id}/turmas", response_model=list[TurmaRead])
def get_docente_turmas(
    usuario_id: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_user),
) -> list[Turma]:
    # Se o usuário não for o próprio docente, deve ser pelo menos um Coordenador (ou Admin)
    if current_user.usuario_id != usuario_id:
        get_current_coordenador(current_user)

    turmas = service.get_turmas(session, usuario_id)
    if turmas is None:
        raise HTTPException(status_code=404, detail="Docente informado não existe")
    return turmas


@router.post("/", response_model=DocenteRead)
def create_docente(
    data: DocenteCreate,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> Docente:
    return service.create_docente(session, data)


@router.patch("/{usuario_id}", response_model=DocenteRead)
def update_docente(
    usuario_id: int,
    data: DocenteUpdate,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> Docente:
    updated = service.update_docente(session, usuario_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Docente não encontrado")
    return updated


@router.delete("/{usuario_id}")
def delete_docente(
    usuario_id: int,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> dict[str, str]:
    docente = session.get(Docente, usuario_id)
    if not docente:
        raise HTTPException(status_code=404, detail="Docente não encontrado")

    success = usuario_service.delete_usuario(session, usuario_id)
    if not success:
        raise HTTPException(status_code=404, detail="Erro ao deletar docente")
    return {"status": "success"}
