# app/schemas/borrow_record.py

from pydantic import BaseModel
from datetime import date
from typing import Optional

class BorrowRecordBase(BaseModel):
    user_id: int
    book_id: int
    borrow_date: date
    return_date: Optional[date] = None  # Optional field for return_date

    class Config:
        orm_mode = True  # This enables compatibility with ORM models (e.g., SQLAlchemy)

class BorrowRecordCreate(BorrowRecordBase):
    pass  # This is used for input validation when creating a new borrow record.

class BorrowRecordOut(BorrowRecordBase):
    id: int  # This class is used for the output response, which includes the record ID.
