# app/schemas/user.py

from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True

    class Config:
        orm_mode = True  # This allows Pydantic models to work with ORMs like SQLAlchemy (if you use them)

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None  # Optional so that users can update any field

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True  # Enables ORM compatibility for the response model
