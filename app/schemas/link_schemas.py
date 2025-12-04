import datetime as dt

from pydantic import BaseModel, HttpUrl, ConfigDict


class CreateLinkSchema(BaseModel):
    title: str | None = None
    original_url: HttpUrl


class LinkSchema(CreateLinkSchema):
    model_config = ConfigDict(from_attributes=True)

    short_code: str
    created_at: dt.datetime
    clicks: int
