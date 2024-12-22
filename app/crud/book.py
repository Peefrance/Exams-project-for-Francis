from typing import List, Optional
from app.schemas.book import BookCreate, BookUpdate, BookOut
from app.models.book import Book

# In-memory storage for books
fake_books_db = {}

def create_book(book: BookCreate) -> BookOut:
    book_id = len(fake_books_db) + 1
    new_book = Book(id=book_id, **book.dict())
    fake_books_db[book_id] = new_book
    return BookOut.from_orm(new_book)

def get_book(book_id: int) -> Optional[BookOut]:
    book = fake_books_db.get(book_id)
    if book:
        return BookOut.from_orm(book)
    return None

def get_books() -> List[BookOut]:
    return [BookOut.from_orm(book) for book in fake_books_db.values()]

def update_book(book_id: int, book: BookUpdate) -> Optional[BookOut]:
    existing_book = fake_books_db.get(book_id)
    if existing_book:
        updated_book = existing_book.copy(update=book.dict(exclude_unset=True))
        fake_books_db[book_id] = updated_book
        return BookOut.from_orm(updated_book)
    return None

def mark_book_unavailable(book_id: int) -> Optional[BookOut]:
    existing_book = fake_books_db.get(book_id)
    if existing_book:
        existing_book.is_available = False
        fake_books_db[book_id] = existing_book
        return BookOut.from_orm(existing_book)
    return None
