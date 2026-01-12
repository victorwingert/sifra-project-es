from typing import Any

from fastapi import APIRouter, Depends
from sqlmodel import Session

from ....db.session import get_session
from ....models import Turma
from ....schemas.discente import DiscenteSchema
from ....schemas.frequencia import FrequenciaRequestSchema
from ....services.frequencia_service import FrequenciaService

router = APIRouter()
service = FrequenciaService()


@router.get("/turmas", response_model=list[Turma])
def get_turmas_ativas(
    docente_id: int, session: Session = Depends(get_session)
) -> list[Turma]:
    return service.get_turmas_docente(session, docente_id)


@router.get("/consultar", response_model=list[Turma])
def get_turmas_ativas_discente(
    discente_id: int, session: Session = Depends(get_session)
) -> list[Turma]:
    return service.get_turmas_discente(session, discente_id)


@router.get("/discentes", response_model=list[DiscenteSchema])
def get_discentes_com_faltas(
    turma_id: int, session: Session = Depends(get_session)
) -> list[DiscenteSchema]:
    return service.get_discentes_com_faltas(session, turma_id)


@router.post("/lancar")
def lancar_frequencia(
    dto: FrequenciaRequestSchema, session: Session = Depends(get_session)
) -> dict[str, Any]:
    return service.lancar_frequencia(session, dto)
