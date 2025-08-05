
from pydantic import BaseModel
from typing import List
from datetime import datetime

class Telemetry(BaseModel):
    vin: str
    latitude: float
    longitude: float
    speed: float
    engine_status: str  # On, Off, Idle
    fuel_level: float
    odometer: float
    diagnostic_codes: List[str] = []
    timestamp: datetime
# GPS coordinates (latitude, longitude)
# Speed (current speed in km/h)
# Engine status (On/Off/Idle)
# Fuel/Battery level (percentage)
# Odometer reading (total kilometers)
# Diagnostic codes (if any errors)
# Timestamp of the reading
 
