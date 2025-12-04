from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user_models import UserModel


async def add(email: str, hashed_pw: str, session: AsyncSession) -> UserModel:
    user = UserModel(
        email=email,
        password=hashed_pw,
    )

    session.add(user)
    await session.commit()

    return user


async def get_by_id(id: int, session: AsyncSession) -> UserModel | None:
    query = select(UserModel).filter_by(id=id)
    user = (await session.execute(query)).scalar_one_or_none()

    return user


async def get_by_email(email: str, session: AsyncSession) -> UserModel | None:
    query = select(UserModel).filter_by(email=email)
    user = (await session.execute(query)).scalar_one_or_none()

    return user
