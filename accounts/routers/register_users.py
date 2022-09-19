from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from accounts import schema, views
from database import get_db

router = APIRouter(
    prefix='/api/v1',
    tags=["Create Users"]
)


@router.post('/register/locum', response_model=schema.User)
def create_locum_user(user: schema.CreateUser, db: Session = Depends(get_db)):
    response = views.create_locum_user(db=db, user=user)
    return response

@router.post('/register/institution', response_model=schema.User)
def create_institution_user(user: schema.CreateUser, db: Session = Depends(get_db)):
    response = views.create_institution_user(db=db, user=user)
    return response