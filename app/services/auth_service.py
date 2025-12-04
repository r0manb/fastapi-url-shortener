import bcrypt
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user_schemas import UserInSchema, UserOutSchema
from app.repositories import user_repository


async def register(user_data: UserInSchema, session: AsyncSession) -> None:
    created_user = await user_repository.get_by_email(user_data.email, session)
    if created_user:
        raise HTTPException(400, "Пользователь с таким email уже существует")

    hashed_pw = bcrypt.hashpw(user_data.password.encode("utf-8"), bcrypt.gensalt())

    await user_repository.add(user_data.email, hashed_pw.decode("utf-8"), session)


async def login(user_data: UserInSchema, session: AsyncSession) -> UserOutSchema:
    user = await user_repository.get_by_email(user_data.email, session)

    if not user:
        raise HTTPException(400, "Неверная пара логин-пароль")

    if not bcrypt.checkpw(
        user_data.password.encode("utf-8"), user.password.encode("utf-8")
    ):
        raise HTTPException(400, "Неверная пара логин-пароль")

    return UserOutSchema.model_validate(user)
