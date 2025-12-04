from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase

from typing import Sequence, Type, TypeVar

_ModelType = TypeVar("_ModelType", bound=DeclarativeBase)
_SchemaType = TypeVar("_SchemaType", bound=BaseModel)


def convert_models_to_schemas(
    models: Sequence[_ModelType], schema: Type[_SchemaType]
) -> tuple[_SchemaType, ...]:
    return tuple(schema.model_validate(model) for model in models)
