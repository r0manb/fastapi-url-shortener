from fastapi import HTTPException
import shortuuid
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.repositories import link_repository
from app.schemas.link_schemas import CreateLinkSchema, LinkSchema
from app.utils import schema_utils

_uuid_generator = shortuuid.ShortUUID()


async def create_link(
    link_data: CreateLinkSchema, user_id: int, session: AsyncSession
) -> LinkSchema:
    short_code = _uuid_generator.random(settings.SHORT_CODE_LEN)

    link = await link_repository.add(
        user_id, link_data.title, link_data.original_url, short_code, session
    )

    return LinkSchema.model_validate(link)


async def get_links(user_id: int, session: AsyncSession) -> tuple[LinkSchema, ...]:
    links = await link_repository.get_many_by_user_id(user_id, session)

    return schema_utils.convert_models_to_schemas(links, LinkSchema)


async def to(short_code: str, session: AsyncSession) -> LinkSchema:
    link = await link_repository.get_by_short_code(short_code, session)

    if not link:
        raise HTTPException(404, "Ссылки не существует")

    link.clicks += 1
    await session.commit()
    await session.refresh(link)

    return LinkSchema.model_validate(link)
