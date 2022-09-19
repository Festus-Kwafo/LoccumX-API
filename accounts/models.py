from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_locum = Column(Boolean, default=False)
    is_institution = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

    #relationships 
    locum = relationship("Locum", back_populates="user")
    institution = relationship("Institution", back_populates="user")

class Locum(Base):
    __tablename__='locum'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    profile_image = Column(String, index=True)
    gender = Column(String, index=True)
    about_me = Column(String, index=True)
    service =  Column(String, index=True)
    cv_file= Column(String, index=True)
    
    user = relationship('User', back_populates='locum')


class Institution(Base):
    __tablename__= "institution"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    location = Column(String, index=True)
    name_of_organisation= Column(String, index=True)
    service = Column(String, index=True)
    license_file = Column(String, index=True)

    user = relationship('User', back_populates='institution')


