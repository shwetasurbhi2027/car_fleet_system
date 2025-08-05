from fastapi import APIRouter, HTTPException
from models.telemetry import Telemetry
from storage.database import telemetry_latest, telemetry_history, vehicles
from utils.alert_generator import generate_alert

router = APIRouter()

@router.post("/")
def receive_telemetry(data: Telemetry):
    if data.vin not in vehicles:
        raise HTTPException(status_code=404, detail="Vehicle not registered")
    
    telemetry_latest[data.vin] = data
    telemetry_history.setdefault(data.vin, []).append(data)

    # Alerts
    if data.speed > 120:
        generate_alert(data.vin, "Speed Violation", "High")
    if data.fuel_level < 15:
        generate_alert(data.vin, "Low Fuel", "Low")

    return {"msg": "Telemetry received"}

@router.get("/{vin}")
def get_latest_telemetry(vin: str):
    if vin not in telemetry_latest:
        raise HTTPException(status_code=404, detail="No data found")
    return telemetry_latest[vin]

