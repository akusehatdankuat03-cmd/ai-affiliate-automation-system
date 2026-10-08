from celery import Celery

celery_app = Celery(
    "affiliate_ai",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

@celery_app.task(name="affiliate_ai.process_research")
def process_research(category: str, keywords: list[str] | None = None):
    return {"status": "queued", "category": category, "keywords": keywords or []}
