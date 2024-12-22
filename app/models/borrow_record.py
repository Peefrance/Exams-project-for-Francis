# app/models/borrow_record.py

from typing import Optional
from datetime import date

class BorrowRecord:
    def __init__(self, id: int, user_id: int, book_id: int, borrow_date: date, return_date: Optional[date] = None):
        self.id = id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date

    def copy(self, update_data: dict):
        """Update the BorrowRecord instance with new data."""
        for key, value in update_data.items():
            setattr(self, key, value)
