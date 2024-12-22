# app/schemas/book.py

from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    is_available: bool = True

    class Config:
        orm_mode = True  # This allows Pydantic models to work with ORMs (if you are using one)

class BookCreate(BookBase):
    pass  # This class is used for creating new books. Inherits from BookBase

class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    is_available: Optional[bool] = None
    # These fields are optional because you may update just one field, not all fields.

class BookOut(BookBase):
    id: int  # This class is used for the output response when retrieving books.

    class Config:
        orm_mode = True  # This allows conversion of ORM models to Pydantic models
