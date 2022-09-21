from sqlalchemy.orm import Session
from datetime import date

from jobs import models, schema
from accounts.schema import User

def create_jobs(request: schema.CreateJob, db: Session, current_user: User):
    new_job = models.Job(title=request.title, location=request.location, name_organization=request.name_organization,  profile_img = request.profile_img, min_salary=request.min_salary, max_salary=request.max_salary, job_type=request.job_type, description=request.description, expiry_date=request.expiry_date, created_by= current_user.id, created_on = date.today() )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

def all_job(db: Session):
    all_jobs = db.query(models.Job).all()
    return all_jobs


