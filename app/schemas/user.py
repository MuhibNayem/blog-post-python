from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserInDBBase(UserBase):
    id: UUID
    is_active: bool

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass
