from fastapi import FastAPI

from src.models import channel_model
from src.models import message_model
from src.models import user_model

from src.routers import message_router
from src.routers import channel_router
from src.routers import user_router

from src.database import db

app = FastAPI()

channel_model.Base.metadata.create_all(bind=db.engine)
message_model.Base.metadata.create_all(bind=db.engine)
user_model.Base.metadata.create_all(bind=db.engine)

app.include_router(message_router.router, tags=['messages'])
app.include_router(channel_router.router, tags=['channels'])
app.include_router(user_router.router, tags=['users'])