from datetime import date
from typing import Union

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str

class CreateUser(UserBase):
    password: str

class User(UserBase):
    id: int
    is_locum: bool
    is_institution: bool
    is_verified: bool
    is_active: bool

    class Config:
        orm_mode = True
        
class UserInDB(User):
    hashed_password: str

class LocumBase(BaseModel):
    profile_image: str
    gender: str
    about_me: Union[str, None] = None
    service = str

class UpdateLocum(LocumBase):
    pass

class Locum(LocumBase):
    id: int
    user_id: int

    class Config:
        orm_mode =True

class InstitutionBase(BaseModel):
    location : str
    name_of_organisation : str
    service : str
    license_file : str

class UpdateInstitution(InstitutionBase):
    pass

class Institution(InstitutionBase):
    id: int
    user_id : int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    email: Union[str, None] = None
    exp: Union[int, None] = None



    



        
