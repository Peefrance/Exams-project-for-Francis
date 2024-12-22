# app/main.py

from fastapi import FastAPI
from app.routes.user import router as user_router
from app.routes.book import router as book_router
from app.routes.borrow_record import router as borrow_record_router

app = FastAPI()

# Include the routes in the main application
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(book_router, prefix="/books", tags=["books"])
app.include_router(borrow_record_router, prefix="/borrow_records", tags=["borrow_records"])
