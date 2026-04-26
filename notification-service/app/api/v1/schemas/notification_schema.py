from pydantic import BaseModel

class NotificationRequest(BaseModel):
    recipient: str
    message: str
    type: str


class NotificationResponse(NotificationRequest):
    id: int

    class Config:
        from_attributes = True