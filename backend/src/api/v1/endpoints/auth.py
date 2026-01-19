from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from ....db.session import get_session
from ....schemas.token import Token
from ....services.auth_service import AuthService

router = APIRouter()
service = AuthService()


@router.post("/token", response_model=Token)
def login_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(get_session)],
) -> Token:
    return service.login(session, form_data.username, form_data.password)
