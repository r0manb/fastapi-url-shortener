from fastapi import APIRouter, Response
from fastapi.responses import RedirectResponse

from app.dependencies.session import SessionDep
from app.services import link_service

router = APIRouter(prefix="/to")


@router.get("/{short_code}", status_code=200)
async def to(short_code: str, session: SessionDep) -> Response:
    link = await link_service.to(short_code, session)

    return RedirectResponse(url=str(link.original_url))
