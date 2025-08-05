import uuid
from models.alert import Alert
from storage.database import alerts_db
from datetime import datetime

def generate_alerts(data):
    if data.speed > 120:
        alerts_db.append(Alert(
            vehicle_id=data.vehicle_id,
            alert_type="Speed Violation",
            severity="High",
            message=f"Speed {data.speed} km/h",
            timestamp=data.timestamp
        ))

    if data.fuel_level is not None and data.fuel_level < 15:
        alerts_db.append(Alert(
            vehicle_id=data.vehicle_id,
            alert_type="Low Fuel",
            severity="Medium",
            message=f"Fuel Level: {data.fuel_level}%",
            timestamp=data.timestamp
        ))

    if data.battery_level is not None and data.battery_level < 15:
        alerts_db.append(Alert(
            vehicle_id=data.vehicle_id,
            alert_type="Low Battery",
            severity="Medium",
            message=f"Battery Level: {data.battery_level}%",
            timestamp=data.timestamp
        ))

    if data.diagnostic_code:
        alerts_db.append(Alert(
            vehicle_id=data.vehicle_id,
            alert_type="Diagnostic Code",
            severity="Critical",
            message=f"Code: {data.diagnostic_code}",
            timestamp=data.timestamp
        ))

