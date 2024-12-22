from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.borrow_record import BorrowRecordOut, BorrowRecordCreate
from app.crud.borrow_record import create_borrow_record, get_borrow_record, get_borrow_records
from app.crud.book import get_book
from app.crud.user import get_user

router = APIRouter()

@router.get("/", response_model=List[BorrowRecordOut])  # Use List here
def read_borrow_records():
    return get_borrow_records()

@router.get("/{record_id}", response_model=BorrowRecordOut)
def read_borrow_record(record_id: int):
    return get_borrow_record(record_id)

@router.post("/", response_model=BorrowRecordOut)
async def create_borrow_record_route(borrow_record: BorrowRecordCreate):
    # Check if the book is available
    book = get_book(borrow_record.book_id)
    if not book or not book.is_available:
        raise HTTPException(
            status_code=400,
            detail="Book is unavailable for borrowing"
        )
    
    # Ensure the user is active
    user = get_user(borrow_record.user_id)
    if not user or not user.is_active:
        raise HTTPException(
            status_code=400,
            detail="User is not active"
        )

    # Ensure the user has not already borrowed the same book
    existing_record = next((
        record for record in fake_borrow_records_db.values()
        if record.user_id == borrow_record.user_id and record.book_id == borrow_record.book_id and record.return_date is None
    ), None)

    if existing_record:
        raise HTTPException(
            status_code=400,
            detail="User has already borrowed this book"
        )

    # Create the borrow record
    return create_borrow_record(borrow_record)

@router.put("/{record_id}", response_model=BorrowRecordOut)
def return_book_route(record_id: int, return_date: str):
    return return_book(record_id, return_date)
