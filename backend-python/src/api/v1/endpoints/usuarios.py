from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ....db.session import get_session
from ....models import Coordenador, Discente, Docente, Usuario
from ....schemas.usuario import UsuarioUpdate
from ....services.usuario_service import UsuarioService
from ..deps import get_current_admin, get_current_user

router = APIRouter()
service = UsuarioService()


@router.get("/me", response_model=Usuario)
def read_user_me(current_user: Usuario = Depends(get_current_user)) -> Usuario:
    return current_user


@router.post("/docente")
def save_docente(
    data: Docente,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> dict[str, str]:
    service.create_docente(session, data)
    return {"status": "success"}


@router.post("/discente")
def save_discente(
    data: Discente,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> dict[str, str]:
    service.create_discente(session, data)
    return {"status": "success"}


@router.post("/coordenador")
def save_coordenador(
    data: Coordenador,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> dict[str, str]:
    service.create_coordenador(session, data)
    return {"status": "success"}


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


@router.delete("/delete/{hero_id}")
def deletar_usuario(
    usuario_id: int,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> dict[str, str]:
    success = service.delete_usuario(session, usuario_id)
    if not success:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"status": "success"}


@router.patch("/{usuario_id}", response_model=Usuario)
def update_usuario(
    usuario_id: int,
    data: UsuarioUpdate,
    session: Session = Depends(get_session),
    _: Usuario = Depends(get_current_admin),
) -> Usuario:
    updated_user = service.update_usuario(session, usuario_id, data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return updated_user
