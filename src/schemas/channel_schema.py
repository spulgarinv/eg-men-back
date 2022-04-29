from datetime import datetime

from pydantic import BaseModel
from pydantic import Field

class ChannelSchema(BaseModel):
    type: str = Field(..., min_length=1, max_length=50)
    name: str = Field(..., min_length=5, max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default=None)

    class Config:
        orm_mode = True