from pydantic import BaseModel, Field, UUID4
from datetime import datetime
from typing import List


class ItemBase(BaseModel):
    text: str = Field(..., min_length=5, max_length=200)


class ItemUpdate(BaseModel):
    text: str | None = Field(default=None, min_length=5, max_length=200)


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: UUID4
    created_at: datetime

    class Config:
        from_attributes = True


class ItemsCollectionResponse(BaseModel):
    items: List[ItemResponse]

    class Config:
        from_attributes = True
