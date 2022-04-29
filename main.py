from fastapi import FastAPI

from models import channel_model
from models import message_model
from models import user_model

from routers import message_router
from routers import channel_router
from routers import user_router

from database import db

BASE_PATH = '/api/v1'

app = FastAPI()

channel_model.Base.metadata.create_all(bind=db.engine)
message_model.Base.metadata.create_all(bind=db.engine)
user_model.Base.metadata.create_all(bind=db.engine)

app.include_router(prefix=BASE_PATH, router=message_router.router, tags=['messages'])
app.include_router(prefix=BASE_PATH, router=channel_router.router, tags=['channels'])
app.include_router(prefix=BASE_PATH, router=user_router.router, tags=['users'])