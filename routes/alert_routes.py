from fastapi import APIRouter, HTTPException
from services.alert_service import (
    get_all_alerts_service,
    get_alert_service
)

router = APIRouter()

@router.get("/")
def get_all_alerts():
    return get_all_alerts_service()

@router.get("/{alert_id}")
def get_alert(alert_id: str):
    alert = get_alert_service(alert_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert
