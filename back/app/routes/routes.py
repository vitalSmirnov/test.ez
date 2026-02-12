from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
import uuid

from ..schemas.schemas import (
    ItemCreate,
    ItemResponse,
    ItemsCollectionResponse,
    ItemUpdate,
)
from ..service import ItemsService
from ..configuration.database import get_db

app = APIRouter(prefix="/api/items")


@app.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    service = ItemsService(db)
    return service.create(item)


@app.get("", response_model=ItemsCollectionResponse, status_code=status.HTTP_200_OK)
def read_items(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    service = ItemsService(db)
    return service.get_collection(skip=skip, limit=limit)


@app.get("/{item_id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
def read_item(item_id: uuid.UUID, db: Session = Depends(get_db)):
    service = ItemsService(db)
    db_item = service.get_by_id(item_id)
    return db_item


@app.put("/{item_id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
def update_item(item_id: uuid.UUID, item: ItemUpdate, db: Session = Depends(get_db)):
    service = ItemsService(db)
    db_item = service.update(item_id, item)
    return db_item


@app.delete(
    "/{item_id}",
    response_model=ItemResponse,
    status_code=status.HTTP_200_OK,
)
def delete_item(item_id: uuid.UUID, db: Session = Depends(get_db)):
    service = ItemsService(db)
    return service.delete(item_id)
