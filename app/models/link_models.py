import datetime as dt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql import func

from app.database import Base


class LinkModel(Base):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    original_url: Mapped[str]
    title: Mapped[str] = mapped_column(nullable=True)
    short_code: Mapped[str]
    created_at: Mapped[dt.datetime] = mapped_column(insert_default=func.now())
    clicks: Mapped[int] = mapped_column(default=0)
