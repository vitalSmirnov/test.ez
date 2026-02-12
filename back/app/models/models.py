from sqlalchemy import String, Uuid, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
import uuid

from ..configuration.database import Base


class Item(Base):
    __tablename__ = "items"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, index=True, default=uuid.uuid4
    )
    text: Mapped[str] = mapped_column(String(200), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now()
    )
