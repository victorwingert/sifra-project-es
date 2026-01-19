from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ....db.session import get_session
from ....models import Coordenador, Turma, Usuario
from ....schemas.coordenador import (
    CoordenadorCreate,
    CoordenadorRead,
    CoordenadorUpdate,
)
from ....schemas.turma import TurmaRead
from ....services.coordenador_service import CoordenadorService
from ....services.docente_service import DocenteService  # Reusing logic if applicable or create CoordenadorService.get_turmas
from ....services.usuario_service import UsuarioService
from ..deps import get_current_admin, get_current_coordenador, get_current_user

router = APIRouter()
service = CoordenadorService()
# Note: Coordinators might view all classes or classes in their department.
# For this fix, assuming they might also be teachers OR we need to fetch turmas they coordinate.
# If they need to see "their" turmas, we need to implement get_turmas in CoordenadorService or reuse DocenteService if they teach.
# Based on the user request, it seems the frontend calls /coordenadores/{id}/turmas.
# Let's add that endpoint.

@router.get("/{usuario_id}/turmas", response_model=list[TurmaRead])
def get_coordenador_turmas(
    usuario_id: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_user),
) -> list[Turma]:
    # Check permissions
    if current_user.usuario_id != usuario_id:
         get_current_coordenador(current_user) # Ensure caller is at least a coordinator

    # IMPLEMENTATION CHOICE:
    # Does a coordinator have "their own" turmas (like a teacher)?
    # Or do they see turmas of their department?
    # Given the frontend call, it treats them like a teacher selection.
    # Let's check if CoordenadorService has get_turmas. It doesn't.
    # We will implement a simple fetch or reuse DocenteService if the coordinator is also a teacher logic,
    # BUT most likely the frontend expects to see classes to manage/view.
    # Let's implementing a 'get_all_turmas' or specific logic.
    # For now, let's look at how DocenteService does it.
    
    # Quick fix: If the coordinator is also a teacher, they have turmas.
    # If not, maybe they want to see ALL turmas?
    # Let's assume for now we want to return ALL turmas for a coordinator to select from,
    # OR we implement get_turmas in service. 
    # Let's update CoordenadorService to have get_turmas.
    
    return service.get_turmas(session, usuario_id)


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
