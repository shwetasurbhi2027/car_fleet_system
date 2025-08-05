from fastapi import APIRouter, HTTPException
from models.vehicle import Vehicle
from services.vehicle_service import (
    add_vehicle_service,
    list_vehicles_service,
    get_vehicle_service,
    delete_vehicle_service
)

router = APIRouter()

@router.post("/")
def add_vehicle(vehicle: Vehicle):
    if not add_vehicle_service(vehicle):
        raise HTTPException(status_code=400, detail="Vehicle already exists")
    return {"msg": "Vehicle added"}

@router.get("/")
def list_vehicles():
    return list_vehicles_service()

@router.get("/{vin}")
def get_vehicle(vin: str):
    vehicle = get_vehicle_service(vin)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.delete("/{vin}")
def delete_vehicle(vin: str):
    deleted = delete_vehicle_service(vin)
    if not deleted:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return {"msg": "Deleted"}
