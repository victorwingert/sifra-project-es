from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ....db.session import get_session
from ....models.discente import Discente
from ....models.turma import Turma
from ....schemas.discente import DiscenteRead
from ....schemas.turma import TurmaRead
from ....services.turma_service import TurmaService

router = APIRouter()
service = TurmaService()


@router.get("/", response_model=list[TurmaRead])
def list_turmas(*, session: Session = Depends(get_session)) -> list[Turma]:
    return service.list_turmas(session)


@router.get("/{turma_id}/discentes", response_model=list[DiscenteRead])
def get_turma_discentes(
    turma_id: int, session: Session = Depends(get_session)
) -> list[Discente]:
    discentes = service.get_discentes(session, turma_id)
    if discentes is None:
        raise HTTPException(status_code=404, detail="Turma não encontrada")

    return [
        {
            **d.model_dump(),
            "id": d.usuario_id,
            "nome": d.usuario.nome,
            "email": d.usuario.email,
            "telefone": d.usuario.telefone,
            "imagem": d.usuario.imagem,
            "tipo_usuario": d.usuario.tipo_usuario,
        }
        for d in discentes
    ]
