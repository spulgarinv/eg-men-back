import pytz
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP

from database.db import Base

TIMEZONE = pytz.timezone('America/Bogota')

class Channel(Base):
    __tablename__ = 'channels'

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now(TIMEZONE))
    updated_at = Column(TIMESTAMP, default=datetime.now(TIMEZONE), onupdate=datetime.now(TIMEZONE))