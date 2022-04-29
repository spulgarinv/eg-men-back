import pytz
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP

from database.db import Base

TIMEZONE = pytz.timezone('America/Bogota')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    cellphone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now(TIMEZONE))
    updated_at = Column(TIMESTAMP, default=datetime.now(TIMEZONE), onupdate=datetime.now(TIMEZONE))