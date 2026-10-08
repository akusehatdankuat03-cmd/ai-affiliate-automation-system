class AffiliateService:
    def check(self, product_name: str, platform: str = "shopee"):
        product_name_lower = product_name.lower()
        affiliate_available = any(keyword in product_name_lower for keyword in ["blender", "brush", "fan"])
        return {
            "platform": platform,
            "product_name": product_name,
            "affiliate_available": affiliate_available,
            "commission_rate": 0.08 if affiliate_available else 0.0,
            "status": "active" if affiliate_available else "not_found",
        }
