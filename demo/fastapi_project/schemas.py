from typing import List
from pydantic import BaseModel

class TagBase(BaseModel):
    name: str

class Tag(TagBase):
    id: int
    images: List['SvgImage'] = []

    class Config:
        orm_mode = True

class SvgImageBase(BaseModel):
    name: str
    width: int
    height: int
    description: str = None

class SvgImage(SvgImageBase):
    id: int
    tags: List[Tag] = []

    class Config:
        orm_mode = True
