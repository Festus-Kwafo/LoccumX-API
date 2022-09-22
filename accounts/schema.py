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

    class Config():
        orm_mode = True
        
class UserInDB(User):
    hashed_password: str

class LocumBase(BaseModel):
    profile_image: str | None = None
    gender: str | None = None
    about_me: str | None = None
    service : str | None = None 

class UpdateLocum(LocumBase):
    pass

class Locum(LocumBase):
    id: int
    user_id: int
    
    class Config():
        orm_mode = True

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

    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
    exp: int | None = None

class UserLocum(BaseModel):
    id : int
    user_id: int
    email : str 
    is_locum : bool
    is_active : bool
    is_verified: bool
    about_me: str | None = None
    gender: str | None = None
    service: str | None = None

class UserInstitution(BaseModel):
    id : int 
    user_id: int
    email : str 
    is_institution : bool
    is_active : bool
    is_verified: bool
    name_of_organisation: str | None = None
    service: str | None = None
    location: str | None = None
    

    



        
