from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime

class PostBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    create_at: Optional[date] = datetime.now().date()
    is_active: Optional[bool] = False


class PostCreate(PostBase):
    title: str
    content: str
    author: str


class ShowPost(PostBase):
    title: str
    content: str
    author: str
    create_at: date

    # Need to get data for relationships. Will be used when we introduce User
    # model.
    class Config():
        orm_mode = True