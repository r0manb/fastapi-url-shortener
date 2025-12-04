from app.config import settings
from app.services.token_service import _TokenService


access_token_service = _TokenService(
    settings.JWT_ACCESS_SECRET_KEY, settings.JWT_ACCESS_EXP
)
