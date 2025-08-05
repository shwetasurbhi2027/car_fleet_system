from fastapi import APIRouter, HTTPException
from models.telemetry import Telemetry
from services.telemetry_service import (
    receive_telemetry_service,
    get_latest_telemetry_service
)

router = APIRouter()

@router.post("/")
def receive_telemetry(data: Telemetry):
    success = receive_telemetry_service(data)
    if not success:
        raise HTTPException(status_code=404, detail="Vehicle not registered")
    return {"msg": "Telemetry received"}

@router.get("/{vin}")
def get_latest_telemetry(vin: str):
    data = get_latest_telemetry_service(vin)
    if not data:
        raise HTTPException(status_code=404, detail="No telemetry found")
    return data



