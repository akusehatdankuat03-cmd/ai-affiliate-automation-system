from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.endpoints import products, media, approvals

app = FastAPI(title=settings.APP_NAME, version="0.1.0", debug=settings.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/api/v1")
app.include_router(media.router, prefix="/api/v1")
app.include_router(approvals.router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": settings.APP_NAME}
