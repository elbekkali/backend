from pydantic import BaseModel, EmailStr
from pydantic import ConfigDict
from typing import Optional
from uuid import UUID
from datetime import date
from enum import Enum


class UserRole(str, Enum):
    admin = "admin"
    agent = "agent"
    client = "client"


class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Optional[str]
    role: UserRole
    status: UserStatus = UserStatus.active
    birth_date: Optional[date]
    address: Optional[str]
    profile_picture: Optional[str]
    notes: Optional[str]


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    role: Optional[UserRole] = None
    status: Optional[UserStatus] = None
    birth_date: Optional[date] = None
    address: Optional[str] = None
    profile_picture: Optional[str] = None
    notes: Optional[str] = None
    password: Optional[str] = None


class UserReplace(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    role: UserRole
    status: UserStatus
    birth_date: date
    address: str
    profile_picture: str
    notes: str
