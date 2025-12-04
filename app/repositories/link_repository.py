from typing import Sequence

from pydantic import HttpUrl
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.link_models import LinkModel


async def add(
    user_id: int,
    title: str | None,
    original_url: HttpUrl,
    short_code: str,
    session: AsyncSession,
) -> LinkModel:
    link = LinkModel(
        user_id=user_id,
        original_url=str(original_url),
        short_code=short_code,
        title=title,
    )

    session.add(link)
    await session.commit()
    await session.refresh(link)

    return link


async def get_many_by_user_id(
    user_id: int, session: AsyncSession
) -> Sequence[LinkModel]:
    query = select(LinkModel).filter_by(user_id=user_id)
    links = (await session.execute(query)).scalars().all()

    return links


async def get_by_short_code(short_code: str, session: AsyncSession) -> LinkModel | None:
    query = select(LinkModel).filter_by(short_code=short_code)
    link = (await session.execute(query)).scalar_one_or_none()

    return link
