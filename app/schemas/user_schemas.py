from pydantic import BaseModel, ConfigDict, EmailStr


class UserBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr


class UserInSchema(UserBaseSchema):
    password: str


class UserOutSchema(UserBaseSchema):
    id: int
