from sqlalchemy import String, ForeignKey, DateTime, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.db.base import Base


class Schedule(Base):
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_id: Mapped[int | None] = mapped_column(ForeignKey("products.id"), nullable=True)
    draft_id: Mapped[int | None] = mapped_column(nullable=True)
    platform: Mapped[str] = mapped_column(String(100), nullable=False)
    scheduled_at: Mapped[datetime] = mapped_column(nullable=False)
    timezone: Mapped[str] = mapped_column(String(100), default="UTC")
    status: Mapped[str] = mapped_column(String(50), default="queued")
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
