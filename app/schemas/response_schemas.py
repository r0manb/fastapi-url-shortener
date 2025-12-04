from typing import Generic, TypeVar

from pydantic import BaseModel

_T = TypeVar("_T")


class ResponseSchema(BaseModel, Generic[_T]):
    message: str
    details: _T | None = None
