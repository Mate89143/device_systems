from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.services import user_service
from app.dependencies.database_dependency import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserResponse])
def get_users(
    role: Optional[str] = Query(None, description="Filtrar por rol (admin/support/user)"),
    is_active: Optional[bool] = Query(None, description="Filtrar por estado activo"),
    db: Session = Depends(get_db)
):
    return user_service.get_all_users(db, role=role, is_active=is_active)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(db, user_id)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.put("/{user_id}", response_model=UserResponse)
def update_user_full(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return user_service.update_user_complete(db, user_id, user)

@router.patch("/{user_id}", response_model=UserResponse)
def update_user_partial(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user_partial(db, user_id, user)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service.delete_user(db, user_id)
    return None