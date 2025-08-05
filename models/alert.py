from pydantic import BaseModel
from datetime import datetime

class Alert(BaseModel):
    alert_id: str
    vin: str
    type: str  # Speed Violation, Low Fuel/Battery
    severity: str  # Low, High
    timestamp: datetime
