from models.vehicle import Vehicle
from models.telemetry import Telemetry
from models.alert import Alert
from datetime import datetime
import uuid

# In-memory databases
vehicles = {}
telemetry_latest = {}
telemetry_history = {}
alerts = {}


dummy_vehicle = Vehicle(
    vin="ABC123456789",
    manufacturer="Tesla",
    model="Model 3",
    fleet_id="Fleet-A",
    owner="Shweta",
    status="Active"
)
vehicles[dummy_vehicle.vin] = dummy_vehicle


dummy_telemetry = Telemetry(
    vin="ABC123456789",
    latitude=28.6139,
    longitude=77.2090,
    speed=130.0,  # Over-speeding
    engine_status="On",
    fuel_level=10.0,  # Low fuel
    odometer=15000.0,
    diagnostic_codes=["P0420"],
    timestamp=datetime.utcnow()
)
telemetry_latest[dummy_telemetry.vin] = dummy_telemetry
telemetry_history[dummy_telemetry.vin] = [dummy_telemetry]


dummy_alert = Alert(
    alert_id=str(uuid.uuid4()),
    vin="ABC123456789",
    type="Speed Violation",
    severity="High",
    timestamp=datetime.utcnow()
)
alerts[dummy_alert.alert_id] = dummy_alert

