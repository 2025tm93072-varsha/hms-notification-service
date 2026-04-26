from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.notification_service import send_notification
from app.api.v1.schemas.notification_schema import NotificationRequest

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def notify(data: NotificationRequest, db: Session = Depends(get_db)):
    return send_notification(db, data)