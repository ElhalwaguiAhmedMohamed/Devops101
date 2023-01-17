from typing import Optional
from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    cost: float
    available_quantity: int


class ItemUpdate(BaseModel):
    name: Optional[str]
    cost: Optional[float]
    available_quantity: Optional[int]
