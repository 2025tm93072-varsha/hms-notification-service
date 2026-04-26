from app.models.notification import Notification
from datetime import datetime

def send_notification(db, data):
    print(f"[{data.type}] Sent to {data.recipient}: {data.message}")

    notification = Notification(
        recipient=data.recipient,
        message=data.message,
        type=data.type,
        created_at=datetime.utcnow()
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return notification