from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session_factory


async def _get_db() -> AsyncGenerator:
    async with async_session_factory() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(_get_db)]
