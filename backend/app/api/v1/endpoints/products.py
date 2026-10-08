from fastapi import APIRouter, HTTPException
from app.schemas.product import ProductResearchRequest, ProductResearchResponse
from app.services.research_service import ProductResearchService

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/research", response_model=ProductResearchResponse)
def research_products(payload: ProductResearchRequest):
    service = ProductResearchService()
    result = service.run_research(payload.category, payload.keywords, payload.platform)
    return result


@router.get("/demo")
def demo_products():
    return {
        "message": "Demo endpoint ready",
        "products": [
            {"title": "Portable Blender", "category": "Kitchen"},
            {"title": "Mini Handheld Fan", "category": "Lifestyle"},
        ],
    }
