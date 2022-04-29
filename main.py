from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import channel_model
from models import message_model
from models import user_model

from routers import message_router
from routers import channel_router
from routers import user_router

from database import db

BASE_PATH = '/api/v1'

app = FastAPI()

""" app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
) """

channel_model.Base.metadata.create_all(bind=db.engine)
message_model.Base.metadata.create_all(bind=db.engine)
user_model.Base.metadata.create_all(bind=db.engine)

app.include_router(message_router.router, prefix=BASE_PATH, tags=['messages'])
app.include_router(channel_router.router, prefix=BASE_PATH, tags=['channels'])
app.include_router(user_router.router, prefix=BASE_PATH, tags=['users'])