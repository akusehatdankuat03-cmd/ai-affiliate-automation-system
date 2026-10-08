from fastapi import APIRouter

router = APIRouter(prefix="/media", tags=["media"])

@router.get("/status")
def media_status():
    return {"status": "ready", "message": "Media pipeline initialized"}
