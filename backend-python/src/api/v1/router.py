from fastapi import APIRouter

from .endpoints import auth, frequencia, turmas, usuarios

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(frequencia.router, prefix="/frequencia", tags=["frequencia"])
api_router.include_router(turmas.router, prefix="/turmas", tags=["turmas"])
api_router.include_router(usuarios.router, prefix="/usuario", tags=["usuario"])
