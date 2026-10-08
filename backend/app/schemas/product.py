from pydantic import BaseModel, Field
from typing import List, Optional


class ProductCandidate(BaseModel):
    title: str
    category: str
    source: str
    source_url: str
    price: Optional[float] = None
    affiliate_available: bool = False
    product_score: float = 0.0
    trend_score: float = 0.0


class ProductResearchRequest(BaseModel):
    category: str = Field(..., min_length=2)
    keywords: List[str] = Field(default_factory=list)
    platform: str = "shopee"


class ProductResearchResponse(BaseModel):
    category: str
    products: List[ProductCandidate]
    total_found: int
