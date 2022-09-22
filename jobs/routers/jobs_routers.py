from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from jobs import schema, views
from database import get_db
from accounts.dependencies import get_current_user
from accounts.schema import User

router = APIRouter(
    prefix='/api/v1',
    tags=['Jobs']
)

@router.post('/create/jobs', summary="Create Jobs only by Institution users only", response_model=schema.Job)
def create_jobs(request: schema.CreateJob, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_institution:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not Authorized to create Jobs",
            headers={"WWW-Authenticate": "Bearer"},
        )
    response = views.create_jobs(request, db, current_user)
    return response

@router.get('/jobs', summary="View are jobs in the System", response_model=List[schema.Job], )
def get_all_jobs(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return views.all_job(db)


    
    
