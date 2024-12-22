from typing import List, Optional
from app.models.borrow_record import BorrowRecord  # Ensure the import is correct
from app.schemas.borrow_record import BorrowRecordCreate, BorrowRecordOut
from datetime import date

# In-memory storage for borrow records
fake_borrow_records_db = {}

def create_borrow_record(borrow_record: BorrowRecordCreate) -> BorrowRecordOut:
    record_id = len(fake_borrow_records_db) + 1
    new_borrow_record = BorrowRecord(id=record_id, **borrow_record.dict())
    fake_borrow_records_db[record_id] = new_borrow_record
    return BorrowRecordOut.from_orm(new_borrow_record)

def get_borrow_record(record_id: int) -> Optional[BorrowRecordOut]:
    borrow_record = fake_borrow_records_db.get(record_id)
    if borrow_record:
        return BorrowRecordOut.from_orm(borrow_record)
    return None

def get_borrow_records() -> List[BorrowRecordOut]:
    return [BorrowRecordOut.from_orm(record) for record in fake_borrow_records_db.values()]

def return_book(record_id: int, return_date: date) -> Optional[BorrowRecordOut]:
    borrow_record = fake_borrow_records_db.get(record_id)
    if borrow_record:
        borrow_record.return_date = return_date
        fake_borrow_records_db[record_id] = borrow_record
        return BorrowRecordOut.from_orm(borrow_record)
    return None
