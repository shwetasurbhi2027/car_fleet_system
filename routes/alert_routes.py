Router()

@router.get("/")
def get_all_alerts():
    return list(alerts.values())

@router.get("/{alert_idfrom fastapi import APIRouter, HTTPException
from storage.database import alerts

router = API}")
def get_alert(alert_id: str):
    if alert_id in alerts:
        return alerts[alert_id]
    raise HTTPException(status_code=404, detail="Alert not found")
