from fastapi import HTTPException
from sqlalchemy.orm import Session

from accounts import models, schema
from accounts.utils import Hash


def get_Locum_user_by_id(db: Session, user_id: int):
    user = db.query(models.Locum.id, models.Locum.user_id, models.User.email,  models.User.is_locum, models.User.is_active, models.User.is_verified, models.Locum.about_me, models.Locum.gender, models.Locum.service).join(models.Locum).filter(models.User.id == user_id).first()
    if not user:
        return -1
    return user

def get_Institution_user_by_id(db: Session, user_id: int):
    user = db.query(models.Institution.id, models.Institution.user_id, models.User.email,  models.User.is_institution, models.User.is_active, models.User.is_verified, models.Institution.service, models.Institution.name_of_organisation, models.Institution.location).join(models.Institution).filter(models.User.id == user_id).first()
    if not user:
        return -1
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_locum_users(db:Session, skip: int = 0, limit: int = 100):
    users = db.query(models.Locum.id, models.Locum.user_id, models.User.email,  models.User.is_locum, models.User.is_active, models.User.is_verified, models.Locum.about_me, models.Locum.gender, models.Locum.service).join(models.Locum).filter(models.Locum.user_id == models.User.id).filter(models.User.is_locum == True).offset(skip).limit(limit).all()
    return users

def get_institution_users(db:Session, skip: int = 0, limit: int = 100):
    users = db.query(models.Institution.id, models.Institution.user_id, models.User.email,  models.User.is_institution, models.User.is_active, models.User.is_verified, models.Institution.service, models.Institution.name_of_organisation, models.Institution.location).join(models.Institution).filter(models.Institution.user_id == models.User.id).filter(models.User.is_institution == True).offset(skip).limit(limit).all()
    return users

def create_locum_user(db: Session, user: schema.CreateUser):
    user_exists = db.query(models.User).filter(models.User.email == user.email).first()
    if user_exists:
        raise HTTPException(404, "User Already Exists") 
    hashed_password = Hash.bcrypt(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, is_locum = True)
    db.add(db_user)
    db.commit()
    db_locum = models.Locum(user_id = db_user.id)
    db.add(db_locum)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_institution_user(db: Session, user: schema.CreateUser):
    user_exists = db.query(models.User).filter(models.User.email == user.email).first()
    if user_exists:
        raise HTTPException(404, "User Already Exists")
    hashed_password = Hash.bcrypt(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, is_institution = True)
    db.add(db_user)
    db.commit()
    db_institution = models.Institution(user_id = db_user.id)
    db.add(db_institution)
    db.commit()
    db.refresh(db_user)
    return db_user