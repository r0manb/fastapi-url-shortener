from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.services import access_token_service
from app.schemas.user_schemas import UserOutSchema

_security = HTTPBearer()


async def _validate_access_token(
    creds: Annotated[HTTPAuthorizationCredentials, Depends(_security)],
) -> UserOutSchema:
    token = creds.credentials

    payload = access_token_service.verify_token(token)
    if not payload:
        raise HTTPException(401, "Нет авторизации")

    return UserOutSchema(**payload)


AuthDep = Annotated[UserOutSchema, Depends(_validate_access_token)]
