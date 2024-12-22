from typing import List, Optional
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.models.user import User

# In-memory storage for users
fake_users_db = {}

def create_user(user: UserCreate) -> UserOut:
    user_id = len(fake_users_db) + 1
    new_user = User(id=user_id, **user.dict())
    fake_users_db[user_id] = new_user
    return UserOut.from_orm(new_user)

def get_user(user_id: int) -> Optional[UserOut]:
    user = fake_users_db.get(user_id)
    if user:
        return UserOut.from_orm(user)
    return None

def get_users() -> List[UserOut]:
    return [UserOut.from_orm(user) for user in fake_users_db.values()]

def update_user(user_id: int, user: UserUpdate) -> Optional[UserOut]:
    existing_user = fake_users_db.get(user_id)
    if existing_user:
        updated_user_data = existing_user.dict(exclude_unset=True)  # Use dict() here
        updated_user = User(**updated_user_data)  # Re-create User instance with updated data
        fake_users_db[user_id] = updated_user
        return updated_user
    return None

def deactivate_user(user_id: int) -> Optional[UserOut]:
    existing_user = fake_users_db.get(user_id)
    if existing_user:
        existing_user.is_active = False
        fake_users_db[user_id] = existing_user
        return UserOut.from_orm(existing_user)
    return None
