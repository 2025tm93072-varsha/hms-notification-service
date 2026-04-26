from fastapi import FastAPI
from app.api.v1.routes import notification_routes

app = FastAPI(title="Notification Service")

app.include_router(notification_routes.router, prefix="/v1/notifications")

@app.get("/health")
def health():
    return {"status": "UP"}