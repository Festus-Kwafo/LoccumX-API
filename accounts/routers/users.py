from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
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

@router.get('/user/locum/{id}', summary="Get locum user by id", response_model=schema.UserLocum)
def get_locum_user(id: int, db: Session = Depends(get_db)):
    response = views.get_Locum_user_by_id(db, id)
    if response == -1:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"There is no user with the id {id}"
        )
    return response

@router.get('/user/institution/{id}', summary="Get Institution user by id", response_model=schema.UserInstitution)
def get_Institution_user(id: int, db: Session = Depends(get_db)):
    response = views.get_Institution_user_by_id(db, id)
    if response == -1:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f"There is no user with the id {id}"
        )
    return response