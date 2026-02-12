from sqlalchemy.orm import Session
from typing import Optional
import uuid

from fastapi import HTTPException

from ..repository.repository import ItemsRepository
from ..schemas import schemas


class ItemsService:
    def __init__(self, db: Session):
        self.repository = ItemsRepository(db)

    def create(self, item: schemas.ItemCreate) -> schemas.ItemResponse:
        db_item = self.repository.create(item)
        return schemas.ItemResponse.model_validate(db_item)

    def get_by_id(self, item_id: uuid.UUID) -> Optional[schemas.ItemResponse]:
        db_item = self.repository.get_by_id(item_id)
        if not db_item:
            raise HTTPException(
                status_code=400, detail=f"Экземпляр с id {item_id} не найден"
            )
        return schemas.ItemResponse.model_validate(db_item)

    def get_collection(
        self, skip: int = 0, limit: int = 20
    ) -> schemas.ItemsCollectionResponse:
        items = self.repository.get_collection(skip=skip, limit=limit)
        return schemas.ItemsCollectionResponse(
            items=[schemas.ItemResponse.model_validate(item) for item in items]
        )

    def update(
        self, item_id: uuid.UUID, item: schemas.ItemUpdate
    ) -> Optional[schemas.ItemResponse]:
        db_item = self.repository.update(item_id, item)
        if not db_item:
            raise HTTPException(
                status_code=400, detail=f"Экземпляр с id {item_id} не найден"
            )
        return schemas.ItemResponse.model_validate(db_item)

    def delete(self, item_id: uuid.UUID) -> Optional[schemas.ItemResponse]:
        db_item = self.repository.delete(item_id)
        if not db_item:
            raise HTTPException(
                status_code=400, detail=f"Экземпляр с id {item_id} не найден"
            )
        return db_item
