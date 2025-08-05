from fastapi import FastAPI
from routes.vehicle_routes import router as vehicle_router
from routes.telemetry_routes import router as telemetry_router
from routes.alert_routes import router as alert_router

app = FastAPI(title="Connected Car Fleet Management System")

app.include_router(vehicle_router, prefix="/vehicles", tags=["Vehicles"])
app.include_router(telemetry_router, prefix="/telemetry", tags=["Telemetry"])
app.include_router(alert_router, prefix="/alerts", tags=["Alerts"])

