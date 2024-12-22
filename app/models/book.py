# app/models/book.py

from pydantic import BaseModel

# Define Book Pydantic schema for input validation
class BookBase(BaseModel):
    title: str
    author: str
    is_available: bool = True

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookOut(BookBase):
    id: int

# The Book model for in-memory database representation
class Book:
    def __init__(self, id: int, title: str, author: str, is_available: bool = True):
        self.id = id
        self.title = title
        self.author = author
        self.is_available = is_available

    # A method to help with updates to book data
    def copy(self, update_data: dict):
        """Update the Book instance with new data."""
        for key, value in update_data.items():
            setattr(self, key, value)
