from pydantic import BaseModel, Field, field_validator
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    support = "support"
    user = "user"

# Modelo para crear usuario (entrada)
class UserCreate(BaseModel):
    name: str = Field(min_length=3, description="Mínimo 3 caracteres")
    email: str
    role: UserRole
    is_active: bool = True

    @field_validator("email")
    def validate_email(cls, v: str) -> str:
        if "@" not in v or "." not in v.split("@")[-1]:
            raise ValueError("Formato de email inválido")
        return v.lower()

# Modelo para actualización parcial (todos opcionales)
class UserUpdatePartial(BaseModel):
    name: Optional[str] = Field(None, min_length=3)
    email: Optional[str] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None

    @field_validator("email")
    def validate_email(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and ("@" not in v or "." not in v.split("@")[-1]):
            raise ValueError("Formato de email inválido")
        return v.lower() if v else v

# Modelo para respuesta (ocultamos datos internos)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True