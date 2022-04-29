from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException

from schemas import message_schema
from models import message_model

from database.db import SessionLocal
from database.db import engine

router = APIRouter(
    prefix='/messages',
    tags=['messages'],
    responses={404: {'description': 'Not Found!'}}
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get('/')
async def read_all(db: Session = Depends(get_db)):
    data = db.query(message_model.Message).all()

    return {
        "data": data
    }

@router.get('/{message_id}')
async def read_message(message_id: int, db: Session = Depends(get_db)):
    message_obj = db.query(message_model.Message)\
                .filter(message_model.Message.id == message_id)\
                .first()
    
    if message_obj != None:
        return message_obj
    raise HTTPException(status_code=404, detail="Message not found")

@router.post('/')
async def create_message(message: message_schema.MessageSchema, db: Session = Depends(get_db)):
    try:
        db_message = message_model.Message(
            subject = message.subject,
            body = message.body,
            status = message.status,
            attachment = message.attachment
        )
        
        db.add(db_message)
        db.commit()
        db.refresh(db_message)

        return {
            'status': 201,
            'transaction': 'Succesfull'
        }
    except BaseException as e:
        raise HTTPException(status_code=404, detail=repr(e))

@router.put('/{message_id}')
async def update_message(message_id: int, message: message_schema.MessageSchema, db: Session = Depends(get_db)):
    try:
        message_obj = db.query(message_model.Message)\
                    .filter(message_model.Message.id == message_id)\
                    .first()

        if message_obj == None:
            raise HTTPException(status_code=404, detail="Message not found")

        message_obj.subject = message.subject
        message_obj.body = message.body
        message_obj.status = message.status.value
        message_obj.attachment = message.attachment

        db.add(message_obj)
        db.commit()

        return {
            'status': 201,
            'transaction': 'Succesfull'
        }
    except BaseException as e:
        raise HTTPException(status_code=404, detail=repr(e))

@router.delete('/{message_id}')
async def delete_message(message_id: int, db: Session = Depends(get_db)):
    try:
        message_obj = db.query(message_model.Message)\
                    .filter(message_model.Message.id == message_id)\
                    .first()

        if message_obj == None:
            raise HTTPException(status_code=404, detail="Message not found")

        db.query(message_model.Message).filter(message_model.Message.id == message_id).delete()
        db.commit()

        return {
            'status': 200,
            'transaction': 'Succesfull'
        }
    except BaseException as e:
        raise HTTPException(status_code=404, detail=repr(e))