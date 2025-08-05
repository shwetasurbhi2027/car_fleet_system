import uuid
from datetime import datetime
from models.alert import Alert
from storage.database import alerts

def generate_alert(vin, type_, severity):
    alert = Alert(
        alert_id=str(uuid.uuid4()),
        vin=vin,
        type=type_,
        severity=severity,
        timestamp=datetime.utcnow()
    )
    alerts[alert.alert_id] = alert
