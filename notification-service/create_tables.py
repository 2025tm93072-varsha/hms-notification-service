from app.db.session import engine, Base
from app.models.notification import Notification

Base.metadata.create_all(bind=engine)

print("Notification tables created")