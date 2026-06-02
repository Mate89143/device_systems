from app.data.users_db import users_db, current_id
from app.schemas.user_schema import UserCreate, UserUpdatePartial
from fastapi import HTTPException, status

def get_user_or_404(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

def get_user_index(user_id: int):
    for i, user in enumerate(users_db):
        if user["id"] == user_id:
            return i
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

def check_email_duplicate(email: str, exclude_user_id: int = None):
    for user in users_db:
        if user["email"] == email and (exclude_user_id is None or user["id"] != exclude_user_id):
            raise HTTPException(status_code=400, detail="El email ya está registrado")

def create_user(user_data: UserCreate):
    global current_id
    check_email_duplicate(user_data.email)
    new_user = {
        "id": current_id,
        "name": user_data.name,
        "email": user_data.email,
        "role": user_data.role,
        "is_active": user_data.is_active,
    }
    users_db.append(new_user)
    current_id += 1
    return new_user

def update_user_complete(user_id: int, user_data: UserCreate):
    idx = get_user_index(user_id)
    check_email_duplicate(user_data.email, exclude_user_id=user_id)
    updated_user = {
        "id": user_id,
        "name": user_data.name,
        "email": user_data.email,
        "role": user_data.role,
        "is_active": user_data.is_active,
    }
    users_db[idx] = updated_user
    return updated_user

def update_user_partial(user_id: int, user_data: UserUpdatePartial):
    idx = get_user_index(user_id)
    existing = users_db[idx].copy()
    update_data = user_data.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No se enviaron campos para actualizar")
    if "email" in update_data:
        check_email_duplicate(update_data["email"], exclude_user_id=user_id)
    existing.update(update_data)
    users_db[idx] = existing
    return existing

def delete_user(user_id: int):
    idx = get_user_index(user_id)
    deleted = users_db.pop(idx)
    return deleted