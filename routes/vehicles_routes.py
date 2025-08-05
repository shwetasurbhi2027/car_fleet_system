from fastapi import APIRouter, HTTPException
from models.vehicle import Vehicle
from storage.database import vehicles

router = APIRouter()

@router.post("/")
def add_vehicle(vehicle: Vehicle):
    if vehicle.vin in vehicles:
        raise HTTPException(status_code=400, detail="Vehicle already exists")
    vehicles[vehicle.vin] = vehicle
    return {"msg": "Vehicle added"}

@router.get("/")
def list_vehicles():
    return list(vehicles.values())

@router.get("/{vin}")
def get_vehicle(vin: str):
    if vin not in vehicles:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicles[vin]

@router.delete("/{vin}")
def delete_vehicle(vin: str):
    if vin in vehicles:
        del vehicles[vin]
        return {"msg": "Deleted"}
    raise HTTPException(status_code=404, detail="Not found")
