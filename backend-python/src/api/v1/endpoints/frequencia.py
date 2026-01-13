from typing import Any

from fastapi import APIRouter, Depends
from sqlmodel import Session

from ....db.session import get_session
from ....schemas.frequencia import DiscenteFaltas, FrequenciaRequestSchema
from ....services.frequencia_service import FrequenciaService

router = APIRouter()
service = FrequenciaService()


@router.get("/discentes", response_model=list[DiscenteFaltas])
def get_discentes_com_faltas(
    turma_id: int, session: Session = Depends(get_session)
) -> list[DiscenteFaltas]:
    return service.get_discentes_com_faltas(session, turma_id)


@router.post("/lancar")
def lancar_frequencia(
    dto: FrequenciaRequestSchema, session: Session = Depends(get_session)
) -> dict[str, Any]:
    return service.lancar_frequencia(session, dto)
