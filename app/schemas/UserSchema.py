from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated


class UserBase(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=50)]
    email: EmailStr

class UserCreate(UserBase):
    password: Annotated[str, Field(min_length=3, max_length=50)]

class UserRead(UserBase):
    id: int
    image_url: str | None = None

    class Config:
        orm_mode = True