from fastapi import APIRouter

router = APIRouter(prefix="/approvals", tags=["approvals"])

@router.get("/status")
def approval_status():
    return {"status": "ready", "message": "Approval workflow active"}
