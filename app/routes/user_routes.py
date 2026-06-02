from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdatePartial, UserRole
from app.services.user_service import create_user, update_user_complete, update_user_partial, delete_user
from app.dependencies.user_dependencies import get_user_by_id, validate_email_unique
from app.data.users_db import users_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
async def get_users(
    role: Optional[UserRole] = Query(None, description="Filtrar por rol"),
    is_active: Optional[bool] = Query(None, description="Filtrar por estado activo/inactivo")
):
    result = users_db
    if role:
        result = [u for u in result if u["role"] == role]
    if is_active is not None:
        result = [u for u in result if u["is_active"] == is_active]
    return result

@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user(user: dict = Depends(get_user_by_id)):
    return user

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_new_user(
    user_data: UserCreate,
    _: str = Depends(lambda email=Depends(lambda: None): None)  # place para inyectar validación de email
):
    # Usamos validación manual desde service para simplificar
    return create_user(user_data)

@router.put("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def update_user_full(
    user_id: int,
    user_data: UserCreate,
    _: dict = Depends(get_user_by_id)  # asegura que existe
):
    return update_user_complete(user_id, user_data)

@router.patch("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def update_user_partial_endpoint(
    user_id: int,
    user_data: UserUpdatePartial,
    _: dict = Depends(get_user_by_id)
):
    return update_user_partial(user_id, user_data)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_endpoint(
    user_id: int,
    _: dict = Depends(get_user_by_id)
):
    delete_user(user_id)
    return None  # 204 No Content