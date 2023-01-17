from typing import Optional
from pydantic import BaseModel


class OrderCreate(BaseModel):
    shopping_cart_id: int
    requested_quantity: str
    total_cost: str
    item_id: int


class OrderUpdate(BaseModel):
    shopping_cart_id: Optional[int]
    requested_quantity: Optional[str]
    total_cost: Optional[str]
    item_id: Optional[int]
