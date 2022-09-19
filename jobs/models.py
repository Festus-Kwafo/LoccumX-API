from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from database import Base

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, index=True)
    profile_img = Column(String, index=True)
    created_by = Column(ForeignKey('users.id'), index=True)
    name_organization = Column(String, index=True)
    title = Column(String, index=True)
    location = Column(String, index=True)
    description = Column(String, index=True)
    min_salary = Column(Float, index=True)
    max_salary = Column(Float, index=True)
    job_type = Column(String, index=True)
    created_on = Column(DateTime, index=True)
    expiry_date = Column(DateTime, index=True)
