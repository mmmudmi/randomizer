from pydantic import BaseModel
from datetime import datetime


class Shop(BaseModel):
    id: int | None = None
    name: str
    description: str
    tag_id: int

    class Config:
        orm_mode = True

class ShopDetails(BaseModel):
    id: int | None = None
    name: str
    description: str
    tag_id: int
    is_drawn: bool
    time_drawn: datetime

    class Config:
        orm_mode = True

class Tag(BaseModel):
    id: int | None = None
    name: str

    class Config:
        orm_mode = True 



    
