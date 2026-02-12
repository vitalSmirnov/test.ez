from sqlalchemy.orm import Session
from typing import Optional, List

from ..models import models
from ..schemas import schemas


class ItemsRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, item: schemas.ItemCreate) -> models.Item:
        db_item = models.Item(text=item.text)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def get_by_id(self, item_id: int) -> Optional[models.Item]:
        return self.db.query(models.Item).filter(models.Item.id == item_id).first()

    def get_collection(self, skip: int = 0, limit: int = 100) -> List[models.Item]:
        return (
            self.db.query(models.Item)
            .order_by(models.Item.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update(self, item_id: int, item: schemas.ItemUpdate) -> Optional[models.Item]:
        db_item = self.get_by_id(item_id)
        if not db_item:
            return None

        if item.text is not None:
            db_item.text = item.text

        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def delete(self, item_id: int) -> Optional[models.Item]:
        db_item = self.get_by_id(item_id)
        if not db_item:
            return None

        self.db.delete(db_item)
        self.db.commit()
        return db_item
