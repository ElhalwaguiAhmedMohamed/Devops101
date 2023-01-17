from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...schemas.items import ItemCreate, ItemUpdate
from ...db.seesion import get_db
from ...db.repository.items import createNewItem, deleteItemById, listItems, retrieveItem, updateItemById

router = APIRouter()


@router.post("/")
def create(item: ItemCreate, db: Session = Depends(get_db)):
    item = createNewItem(item, db)
    return item


@router.get("/")
def find(db: Session = Depends(get_db)):
    items = listItems(db)
    return items


@router.get("/{id}")
def find_by_id(id: int, db: Session = Depends(get_db)):
    item = retrieveItem(id, db)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with this id {id} does not exist")
    return item


@router.put("/{id}")
def update(id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    message = updateItemById(id, item, db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {id} not found")
    return {"msg": "Successfully updated data."}


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    message = deleteItemById(id, db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {id} not found")
    return {"msg": "Successfully deleted."}
