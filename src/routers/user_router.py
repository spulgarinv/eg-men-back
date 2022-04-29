from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException

from schemas import user_schema
from models import user_model

from database.db import SessionLocal
from database.db import engine

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not Found!'}}
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
user_model.Base.metadata.create_all(bind=engine)

@router.get('/')
async def read_all(db: Session = Depends(get_db)):
    data = db.query(user_model.User).all()

    return {
        "data": data
    }

@router.get('/{user_id}')
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user_obj = db.query(user_model.User)\
                .filter(user_model.User.id == user_id)\
                .first()
    
    if user_obj != None:
        return user_obj
    raise HTTPException(status_code=404, detail="Message not found")

@router.post('/')
async def create_user(user: user_schema.UserSchema, db: Session = Depends(get_db)):
    try:
        db_user = user_model.User(
            name = user.name,
            type = user.type.value,
            cellphone_number = user.cellphone_number,
            email = user.email,
            gender = user.gender.value
        )
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return {
            'status': 201,
            'transaction': 'Succesfull'
        }
    except BaseException as e:
        raise HTTPException(status_code=404, detail=repr(e))

@router.put('/{user_id}')
async def update_user(user_id: int, user: user_schema.UserSchema, db: Session = Depends(get_db)):
    try:
        user_obj = db.query(user_model.User)\
                    .filter(user_model.User.id == user_id)\
                    .first()

        if user_obj == None:
            raise HTTPException(status_code=404, detail="Message not found")

        user_obj.name = user.name
        user_obj.type = user.type.value
        user_obj.cellphone_number = user.cellphone_number
        user_obj.email = user.email
        user_obj.gender = user.gender.value

        db.add(user_obj)
        db.commit()

        return {
            'status': 201,
            'transaction': 'Succesfull'
        }
    except BaseException as e:
        raise HTTPException(status_code=404, detail=repr(e))

@router.delete('/{user_id}')
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user_obj = db.query(user_model.User)\
                    .filter(user_model.User.id == user_id)\
                    .first()

        if user_obj == None:
            raise HTTPException(status_code=404, detail="Message not found")

        db.query(user_model.User).filter(user_model.User.id == user_id).delete()
        db.commit()

        return {
            'status': 200,
            'transaction': 'Succesfull'
        }
    except BaseException as e:
        raise HTTPException(status_code=404, detail=repr(e))