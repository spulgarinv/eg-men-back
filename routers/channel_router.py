from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException

from schemas import channel_schema
from models import channel_model

from database.db import SessionLocal
from database.db import engine

router = APIRouter(
    prefix='/channels',
    tags=['channels'],
    responses={404: {'description': 'Not Found!'}}
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
channel_model.Base.metadata.create_all(bind=engine)

@router.get('/')
async def read_all(db: Session = Depends(get_db)):
    data = db.query(channel_model.Channel).all()

    return {
        "data": data
    }

@router.get('/{channel_id}')
async def read_channel(channel_id: int, db: Session = Depends(get_db)):
    channel_obj = db.query(channel_model.Channel)\
                .filter(channel_model.Channel.id == channel_id)\
                .first()
    
    if channel_obj != None:
        return channel_obj
    raise HTTPException(status_code=404, detail="Message not found")

@router.post('/')
async def create_channel(channel: channel_schema.ChannelSchema, db: Session = Depends(get_db)):
    try:
        db_channel = channel_model.Channel(
            type = channel.type,
            name = channel.name
        )
        
        db.add(db_channel)
        db.commit()
        db.refresh(db_channel)

        return {
            'status': 201,
            'transaction': 'Succesfull'
        }
    except BaseException as e:
        raise HTTPException(status_code=404, detail=repr(e))

@router.put('/{channel_id}')
async def update_channel(channel_id: int, channel: channel_schema.ChannelSchema, db: Session = Depends(get_db)):
    try:
        channel_obj = db.query(channel_model.Channel)\
                    .filter(channel_model.Channel.id == channel_id)\
                    .first()

        if channel_obj == None:
            raise HTTPException(status_code=404, detail="Message not found")

        channel_obj.type = channel.type
        channel_obj.name = channel.name

        db.add(channel_obj)
        db.commit()

        return {
            'status': 201,
            'transaction': 'Succesfull'
        }
    except BaseException as e:
        raise HTTPException(status_code=404, detail=repr(e))

@router.delete('/{channel_id}')
async def delete_channel(channel_id: int, db: Session = Depends(get_db)):
    try:
        channel_obj = db.query(channel_model.Channel)\
                    .filter(channel_model.Channel.id == channel_id)\
                    .first()

        if channel_obj == None:
            raise HTTPException(status_code=404, detail="Message not found")

        db.query(channel_model.Channel).filter(channel_model.Channel.id == channel_id).delete()
        db.commit()

        return {
            'status': 200,
            'transaction': 'Succesfull'
        }
    except BaseException as e:
        raise HTTPException(status_code=404, detail=repr(e))