from storage.database import alerts

def get_all_alerts_service():
    return list(alerts.values())

def get_alert_service(alert_id: str):
    return alerts.get(alert_id)

