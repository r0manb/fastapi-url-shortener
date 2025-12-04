from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config import settings


class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    settings.DB_URL,
    # echo=True,
    pool_size=6,
)
async_session_factory = async_sessionmaker(engine)
