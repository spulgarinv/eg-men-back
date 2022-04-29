import pytz
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP

from database.db import Base

TIMEZONE = pytz.timezone('America/Bogota')

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    body = Column(String, nullable=False)
    status = Column(String, nullable=False)
    attachment = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.now(TIMEZONE))
    updated_at = Column(TIMESTAMP, default=datetime.now(TIMEZONE), onupdate=datetime.now(TIMEZONE))