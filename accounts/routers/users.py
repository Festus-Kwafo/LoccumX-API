from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from accounts import schema, views
from accounts.dependencies import get_current_user
from database import get_db

router = APIRouter(
    prefix='/api/v1',
    tags=["Users"]
)

@router.get('/users/locum', summary="Get All locum users", response_model=List[schema.UserLocum])
def get_all_locum(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    response = views.get_locum_users(db)
    return response

@router.get("/users/institution", summary="Get all Institution users", response_model=List[schema.UserInstitution])
def get_all_institution(db: Session=Depends(get_db), current_user = Depends(get_current_user)):
    response = views.get_institution_users(db)
    return response

@router.post('/register/locum', response_model=schema.User)
def create_locum_user(user: schema.CreateUser, db: Session = Depends(get_db)):
    response = views.create_locum_user(db=db, user=user)
    return response

@router.post('/register/institution', response_model=schema.User)
def create_institution_user(user: schema.CreateUser, db: Session = Depends(get_db)):
    response = views.create_institution_user(db=db, user=user)
    return response
