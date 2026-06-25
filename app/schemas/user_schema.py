from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    admin = "admin"
    support = "support"
    user = "user"

# Schemas de entrada (API)

class UserCreate(BaseModel):
    name: str = Field(min_length=3, description="Mínimo 3 caracteres")
    email: EmailStr   # validación automática de email
    role: UserRole
    is_active: bool = True

    @field_validator("name")
    def capitalize_name(cls, v: str) -> str:
        return v.strip().title()

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3)
    email: Optional[EmailStr] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None

# Schema de respuesta (salida)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: UserRole
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True   # permite convertir desde modelo SQLAlchemy