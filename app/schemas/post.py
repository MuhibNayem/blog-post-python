from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class PostInDBBase(PostBase):
    id: UUID
    owner_id: UUID

    class Config:
        orm_mode = True

class Post(PostInDBBase):
    pass
