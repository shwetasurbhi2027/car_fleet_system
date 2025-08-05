from models.telemetry import Telemetry
from storage.database import telemetry_latest, telemetry_history, vehicles
from utils.alert_generator import generate_alert

def receive_telemetry_service(data: Telemetry):
    if data.vin not in vehicles:
        return False

    telemetry_latest[data.vin] = data
    telemetry_history.setdefault(data.vin, []).append(data)

    # Business rules for generating alerts
    if data.speed > 120:
        generate_alert(data.vin, "Speed Violation", "High")
    if data.fuel_level < 15:
        generate_alert(data.vin, "Low Fuel", "Low")

    return True

def get_latest_telemetry_service(vin: str):
    return telemetry_latest.get(vin)

