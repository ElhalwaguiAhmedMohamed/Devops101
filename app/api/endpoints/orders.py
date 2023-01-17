from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...schemas.orders import OrderCreate, OrderUpdate
from ...db.seesion import get_db
from ...db.repository.orders import createNewOrder, deleteOrderById, listOrders, retrieveOrder, updateOrderById
from ...db.repository.items import retrieveItem

router = APIRouter()


@router.post("/")
def create(order: OrderCreate, db: Session = Depends(get_db)):
    item = retrieveItem(order.item_id, db)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with this id {order.item_id} does not exist")
    if int(order.requested_quantity) > int(item.available_quantity):
        raise HTTPException(
            status_code=422, detail=f"Order quantity cannot be more than {item.available_quantity}")
    order = createNewOrder(order, db)
    return order


@router.get("/")
def find(db: Session = Depends(get_db)):
    orders = listOrders(db=db)
    return orders


@router.get("/{id}")
def find_by_id(id: int, db: Session = Depends(get_db)):
    order = retrieveOrder(id, db)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with this id {id} does not exist")
    return order


@router.put("/{id}")
def update(id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    if order.item_id:
        new_item = retrieveItem(order.item_id, db)
        if not new_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Order with this id {order.item_id} does not exist")
    if order.requested_quantity:
        old_order = retrieveOrder(id, db)
        old_item = retrieveItem(old_order.item_id, db)
        if int(order.requested_quantity) > int(old_item.available_quantity):
            raise HTTPException(
                status_code=422, detail=f"Order quantity cannot be more than {old_item.available_quantity}")
    message = updateOrderById(id, order, db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with id {id} not found")
    return {"msg": "Successfully updated data."}


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    message = deleteOrderById(id, db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with id {id} not found")
    return {"msg": "Successfully deleted."}
