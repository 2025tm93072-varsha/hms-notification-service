from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.session import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    recipient = Column(String)
    message = Column(String)
    type = Column(String)  # EMAIL / SMS
    created_at = Column(DateTime, default=datetime.utcnow)