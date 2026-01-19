from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlmodel import Session, select

from ...core.config import settings
from ...db.session import get_session
from ...models.usuario import Usuario
from ...schemas.token import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


def get_current_user(
    session: Annotated[Session, Depends(get_session)],
    token: Annotated[str, Depends(oauth2_scheme)],
) -> Usuario:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(  # type: ignore
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email = payload.get("sub")
        if not isinstance(email, str) or not email:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError as exc:
        raise credentials_exception from exc

    statement = select(Usuario).where(Usuario.email == token_data.email)
    user = session.exec(statement).first()

    if user is None:
        raise credentials_exception
    return user


def get_current_admin(
    current_user: Annotated[Usuario, Depends(get_current_user)],
) -> Usuario:
    if current_user.tipo_usuario != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="O usuário não tem privilégios suficientes",
        )
    return current_user


def get_current_coordenador(
    current_user: Annotated[Usuario, Depends(get_current_user)],
) -> Usuario:
    if (
        current_user.tipo_usuario != "COORDENADOR"
        and current_user.tipo_usuario != "ADMIN"
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso restrito a coordenadores",
        )
    return current_user
