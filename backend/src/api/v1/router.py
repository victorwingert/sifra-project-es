from fastapi import APIRouter

from .endpoints import (
    administradores,
    auth,
    coordenadores,
    discentes,
    docentes,
    frequencia,
    turmas,
    usuarios,
)

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(frequencia.router, prefix="/frequencia", tags=["frequencia"])
api_router.include_router(turmas.router, prefix="/turmas", tags=["turmas"])
api_router.include_router(usuarios.router, prefix="/usuario", tags=["usuario"])
api_router.include_router(
    administradores.router, prefix="/administradores", tags=["administradores"]
)
api_router.include_router(docentes.router, prefix="/docentes", tags=["docentes"])
api_router.include_router(discentes.router, prefix="/discentes", tags=["discentes"])
api_router.include_router(
    coordenadores.router, prefix="/coordenadores", tags=["coordenadores"]
)
