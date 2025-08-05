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
    vin="ABC123",
    manufacturer="BMW",
    model="Model 1",
    fleet_id="Fleet-X",
    owner="Shweta",
    status="Active"
)
vehicles[dummy_vehicle.vin] = dummy_vehicle


dummy_telemetry = Telemetry(
    vin="ABC123",
    latitude=25.00,
    longitude=75.00,
    speed=180.0,  # Over-speeding
    engine_status="On",
    fuel_level=1.0,  # Low fuel
    odometer=1000000.0,
    diagnostic_codes=["P0420"],
    timestamp=datetime.utcnow()
)
telemetry_latest[dummy_telemetry.vin] = dummy_telemetry
telemetry_history[dummy_telemetry.vin] = [dummy_telemetry]


dummy_alert = Alert(
    alert_id=str(uuid.uuid4()),
    vin="ABC123",
    type="Speed Violation",
    severity="High",
    timestamp=datetime.utcnow()
)
alerts[dummy_alert.alert_id] = dummy_alert

