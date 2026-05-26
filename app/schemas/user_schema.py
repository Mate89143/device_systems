from pydantic import BaseModel, Field, field_validator
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    support = "support"
    user = "user"

# Modelo para crear usuario (entrada)
class UserCreate(BaseModel):
    name: str = Field(min_length=3, description="Nombre del usuario, mínimo 3 caracteres")
    email: str = Field(description="Correo electrónico con formato válido")
    role: UserRole = Field(description="Rol permitido: admin, support, user")
    is_active: bool = Field(default=True, description="Estado del usuario")

    @field_validator("email")
    def validate_email(cls, v: str) -> str:
        if "@" not in v or "." not in v.split("@")[-1]:
            raise ValueError("Formato de email inválido")
        return v.lower()

# Modelo para respuesta (ocultamos datos no necesarios)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True  # Permite trabajar con objetos o dicts