class CaptionService:
    def generate_variants(self, product_title: str):
        return [
            {
                "variant": "hook",
                "caption": f"🚀 {product_title} yang lagi viral! Cocok banget buat daily use. Klik link di bio untuk cek detailnya.",
                "hashtags": "#viral #productfind #dailyuse #recommendation",
            },
            {
                "variant": "review",
                "caption": f"Review singkat: {product_title} simpel, fungsional, dan worth it. Cek sebelum stok habis!",
                "hashtags": "#review #musttry #shoppingfinds #affiliate",
            },
            {
                "variant": "problem_solution",
                "caption": f"Punya masalah saat kerja/rumah? {product_title} solusi praktis yang bikin lebih mudah. Cek sekarang!",
                "hashtags": "#problemssolved #bestbuy #rekomendasi #product",
            },
        ]
