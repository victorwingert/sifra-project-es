from fastapi import APIRouter
from app.services.turma_service import get_turmas

router = APIRouter()
@router.get("/")
def list_turmas():
    return get_turmas()