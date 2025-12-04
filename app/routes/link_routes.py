from fastapi import APIRouter

from app.dependencies.session import SessionDep
from app.dependencies.auth import AuthDep
from app.services import link_service
from app.schemas.link_schemas import CreateLinkSchema, LinkSchema
from app.schemas.response_schemas import ResponseSchema

router = APIRouter(prefix="/links")


@router.post("/", status_code=201)
async def create_link(
    body: CreateLinkSchema, token_data: AuthDep, session: SessionDep
) -> ResponseSchema[LinkSchema]:
    link = await link_service.create_link(body, token_data.id, session)

    return ResponseSchema(message="Ссылка успешно создана", details=link)


@router.get("/", status_code=200)
async def get_links(token_data: AuthDep, session: SessionDep) -> tuple[LinkSchema, ...]:
    links = await link_service.get_links(token_data.id, session)

    return links
