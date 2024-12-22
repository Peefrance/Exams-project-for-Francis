from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.crud.user import create_user, get_user, get_users, update_user, deactivate_user

router = APIRouter()

@router.post("/", response_model=UserOut)
async def create_new_user(user: UserCreate):
    return create_user(user)

@router.get("/{user_id}", response_model=UserOut)
async def read_user(user_id: int):
    db_user = get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=List[UserOut])
async def read_users():
    return get_users()

@router.put("/{user_id}", response_model=UserOut)
async def update_existing_user(user_id: int, user: UserUpdate):
    db_user = get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not db_user.is_active:
        raise HTTPException(status_code=400, detail="Cannot update an inactive user")
    
    updated_user = update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=400, detail="User update failed")
    
    return updated_user

@router.delete("/{user_id}", response_model=UserOut)
async def deactivate_existing_user(user_id: int):
    db_user = deactivate_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
