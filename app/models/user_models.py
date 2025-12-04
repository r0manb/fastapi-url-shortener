from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from app.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str]
