from datetime import timedelta

from fastapi import HTTPException, status
from sqlmodel import Session, select

from ..core import security
from ..core.config import settings
from ..models.usuario import Usuario
from ..schemas.token import Token


class AuthService:
    def login(self, session: Session, username: str, password: str) -> Token:
        statement = select(Usuario).where(Usuario.email == username)
        usuario = session.exec(statement).first()

        if not usuario or not security.verify_password(password, usuario.senha):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email ou senha incorretos",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = security.create_access_token(
            subject=usuario.email, expires_delta=access_token_expires
        )

        return Token(access_token=access_token, token_type="bearer")  # noqa: S106
