from datetime import datetime
from typing import Optional
from enum import Enum

from pydantic import BaseModel
from pydantic import Field

class MessageStatus(Enum):
    created = 'created'
    sent = 'sent'
    delivered = 'delivered'
    undelivered = 'undelivered'
    failed = 'failed'

class MessageSchema(BaseModel):
    subject: str = Field(..., min_length=5, max_length=50)
    body: str = Field(..., min_length=10, max_length=200)
    status: Optional[MessageStatus] = Field(default=MessageStatus.created.value)
    attachment: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default=None)

    class Config:
        orm_mode = True