from datetime import datetime
from enum import Enum

from pydantic import BaseModel
from pydantic import Field

class UserGender(Enum):
    male = 'male'
    female = 'female'

class UserType(Enum):
    sender = 'sender'
    recipient = 'recipient'    

class UserSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=30)
    type: UserType = Field(...)
    cellphone_number: str = Field(..., min_length=5, max_length=20)
    email: str = Field(..., min_length=1, max_length=30)
    gender: UserGender = Field(...)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default=None)

    class Config:
        orm_mode = True