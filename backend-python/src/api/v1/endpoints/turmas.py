from fastapi import APIRouter, Depends
from sqlmodel import Session

from ....db.session import get_session
from ....models.turma import Turma
from ....services.turma_service import TurmaService

router = APIRouter()
service = TurmaService()


@router.get("/")
def list_turmas(*, session: Session = Depends(get_session)) -> list[Turma]:
    return service.list_turmas(session)
