from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from app.services.media_service import MediaService

router = APIRouter(prefix="/media", tags=["media"])


@router.get("/status")
def media_status():
    return {"status": "ready", "message": "Media pipeline initialized"}


@router.get("/assets")
def list_assets():
    service = MediaService()
    return {"assets": service.list_assets()}


@router.post("/download")
def download_asset(payload: dict):
    url = payload.get("url")
    if not url:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="URL is required")

    service = MediaService()
    return service.download_asset(url, payload.get("target_dir", "media"))
