from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from app.dependencies.session import SessionDep
from app.services import access_token_service, auth_service
from app.schemas.user_schemas import UserInSchema

router = APIRouter(prefix="/auth")


@router.post("/register", status_code=201)
async def register_user(
    body: UserInSchema,
    session: SessionDep,
) -> Response:
    await auth_service.register(body, session)

    return JSONResponse(content={"message": "Пользователь успешно создан"})


@router.post("/login", status_code=200)
async def login_user(
    body: UserInSchema,
    session: SessionDep,
) -> Response:
    found_user = await auth_service.login(body, session)
    token = access_token_service.generate_token(found_user.model_dump())

    return JSONResponse(content={"message": "Успешная авторизация!", "token": token})
