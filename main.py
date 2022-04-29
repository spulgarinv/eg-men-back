from fastapi import FastAPI

from models import channel_model
from models import message_model
from models import user_model

from routers import message_router
from routers import channel_router
from routers import user_router

from database import db

app = FastAPI(root_path='/api/v1')

channel_model.Base.metadata.create_all(bind=db.engine)
message_model.Base.metadata.create_all(bind=db.engine)
user_model.Base.metadata.create_all(bind=db.engine)

app.include_router(message_router.router, tags=['messages'])
app.include_router(channel_router.router, tags=['channels'])
app.include_router(user_router.router, tags=['users'])