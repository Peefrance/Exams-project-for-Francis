from pydantic import BaseModel

# Define User Pydantic schema for input validation
class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserOut(UserBase):
    id: int

# In-memory User model as Pydantic model (modified)
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
