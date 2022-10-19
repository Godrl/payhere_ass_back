from typing import Optional, Sequence
from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    email: str


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# Properties to receive via API on update
class UserUpdate(BaseModel):
    current_password: Optional[str] = None
    new_password: Optional[str] = None


class UserInfoAuth(BaseModel):
    password: str


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UserInDB(UserInDBBase):
    password: str


class User(UserInDBBase):
    email: str
    created_at: datetime


class UserInfo(UserInDBBase):
    pass


class UserList(BaseModel):
    users: Sequence[User]
    total_count: int
