from fastapi import APIRouter
from .v1 import items, orders

api_router = APIRouter()
api_router.include_router(items.router, prefix='/items', tags=['items'])
api_router.include_router(orders.router, prefix='/orders', tags=['orders'])
