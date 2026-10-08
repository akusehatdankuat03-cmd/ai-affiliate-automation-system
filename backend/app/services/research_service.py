from app.services.affiliate_service import AffiliateService


class ProductResearchService:
    def run_research(self, category: str, keywords: list[str], platform: str):
        affiliated = AffiliateService()
        items = [
            {"title": "Portable Blender", "category": "Kitchen & Daily Use", "source": "China market", "source_url": "https://example.com/product/blender", "price": 129000, "affiliate_available": True},
            {"title": "Mini Desk Fan", "category": "Lifestyle & Mini Appliances", "source": "TikTok trend", "source_url": "https://example.com/product/fan", "price": 89000, "affiliate_available": False},
            {"title": "Smart Electric Toothbrush", "category": "Beauty & Personal Care", "source": "Shopee trend", "source_url": "https://example.com/product/toothbrush", "price": 210000, "affiliate_available": True},
        ]

        candidates = []
        for idx, item in enumerate(items, start=1):
            affiliate_state = affiliated.check(item["title"], platform)
            score = 76 + idx * 4 + (10 if affiliate_state["affiliate_available"] else 0)
            candidates.append({
                "title": item["title"],
                "category": item["category"],
                "source": item["source"],
                "source_url": item["source_url"],
                "price": item["price"],
                "affiliate_available": affiliate_state["affiliate_available"],
                "product_score": round(score, 1),
                "trend_score": round(score / 1.2, 1),
            })

        return {
            "category": category,
            "products": candidates,
            "total_found": len(candidates),
        }
