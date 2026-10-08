from celery import Celery

celery_app = Celery(
    "affiliate_ai",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

@celery_app.task(name="affiliate_ai.health_check")
def health_check():
    return {"status": "ok", "message": "Celery worker ready"}
