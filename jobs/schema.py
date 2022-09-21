from datetime import datetime, date
from pydantic import BaseModel

class JobBase(BaseModel):
    id: int
    title : str 
    location: str
    name_organization: str

class CreateJob(JobBase):
    profile_img : str
    min_salary: float
    max_salary : float
    job_type :  str
    description: str | None
    expiry_date: date

class Job(CreateJob):

    created_by: int
    created_on: datetime

    class Config():
        orm_mode = True

