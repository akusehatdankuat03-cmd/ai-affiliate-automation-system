from sqlalchemy import String, Text, Float, Boolean, JSON, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    source_name: Mapped[str] = mapped_column(String(255), nullable=False)
    external_product_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    price: Mapped[float | None] = mapped_column(Float, nullable=True)
    currency: Mapped[str] = mapped_column(String(20), default="IDR")
    source_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    image_urls: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)
    video_urls: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)
    affiliate_available: Mapped[bool] = mapped_column(Boolean, default=False)
    affiliate_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    commission_rate: Mapped[float | None] = mapped_column(Float, nullable=True)
    commission_details: Mapped[str | None] = mapped_column(Text, nullable=True)
    product_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    trend_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    search_volume_estimate: Mapped[int | None] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="draft")
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    media_assets = relationship("MediaAsset", back_populates="product")
