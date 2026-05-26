from fastapi import APIRouter, HTTPException, Query, Path
from typing import List, Optional
from app.schemas.user_schema import UserCreate, UserResponse, UserRole

router = APIRouter()

# Base de datos simulada en memoria
fake_db = []
current_id = 1

@router.get("/users", response_model=List[UserResponse])
async def get_users(
    role: Optional[UserRole] = Query(None, description="Filtrar por rol"),
    is_active: Optional[bool] = Query(None, description="Filtrar por estado activo/inactivo")
):
    """
    Lista todos los usuarios. Permite filtrar por role y/o is_active.
    """
    result = fake_db
    if role:
        result = [u for u in result if u["role"] == role]
    if is_active is not None:
        result = [u for u in result if u["is_active"] == is_active]
    return result

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user_by_id(user_id: int = Path(..., ge=1, description="ID del usuario")):
    """
    Obtiene un usuario por su ID.
    """
    for user in fake_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@router.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user_data: UserCreate):
    """
    Crea un nuevo usuario. Valida datos y evita emails duplicados.
    """
    global current_id
    # Verificar email duplicado
    for user in fake_db:
        if user["email"] == user_data.email:
            raise HTTPException(status_code=400, detail="El email ya está registrado")
    
    new_user = {
        "id": current_id,
        "name": user_data.name,
        "email": user_data.email,
        "role": user_data.role,
        "is_active": user_data.is_active,
    }
    fake_db.append(new_user)
    current_id += 1
    return new_user