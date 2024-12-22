from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.book import BookCreate, BookUpdate, BookOut
from app.crud.book import create_book, get_book, get_books, update_book, mark_book_unavailable  # Import the correct function

router = APIRouter()

@router.post("/", response_model=BookOut)
async def create_new_book(book: BookCreate):
    return create_book(book)

@router.get("/{book_id}", response_model=BookOut)
async def read_book(book_id: int):
    db_book = get_book(book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.get("/", response_model=List[BookOut])
async def read_books():
    return get_books()

@router.put("/{book_id}", response_model=BookOut)
async def update_existing_book(book_id: int, book: BookUpdate):
    db_book = update_book(book_id, book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/unavailable/{book_id}", response_model=BookOut)
async def mark_book_as_unavailable(book_id: int):
    db_book = mark_book_unavailable(book_id)  # Correct function usage here
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
