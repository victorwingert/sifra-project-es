from fastapi import APIRouter
from .endpoints import turmas


api_router = APIRouter()
api_router.include_router(turmas.router, prefix="/turmas")