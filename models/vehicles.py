from pydantic import BaseModel

class Vehicle(BaseModel):
    vin: str
    manufacturer: str
    model: str
    fleet_id: str
    owner: str
    status: str  

# VIN (Vehicle Identification Number) - unique identifier
# Manufacturer and Model
# Fleet ID (vehicles can belong to different fleets like "Corporate", "Rental", "Personal")
# Owner/Operator information
# Registration status (Active, Maintenance, Decommissioned)

