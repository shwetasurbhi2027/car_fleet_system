from models.vehicle import Vehicle
from storage.database import vehicles

def add_vehicle_service(vehicle: Vehicle):
    if vehicle.vin in vehicles:
        return False
    vehicles[vehicle.vin] = vehicle
    return True

def list_vehicles_service():
    return list(vehicles.values())

def get_vehicle_service(vin: str):
    return vehicles.get(vin)

def delete_vehicle_service(vin: str):
    return vehicles.pop(vin, None)

