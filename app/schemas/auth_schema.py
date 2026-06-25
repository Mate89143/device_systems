from pydantic import BaseModel, Field, field_validator
import re

class UserRegister(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: str = Field(pattern=r'^[^@]+@[^@]+\.[^@]+$')
    password: str = Field(min_length=8)
    role: str = Field(default="user", pattern=r'^(admin|support|user)$')

    @field_validator('password')
    def validate_password(cls, v):
        if not re.search(r'[A-Z]', v):
            raise ValueError('Debe tener al menos una mayúscula')
        if not re.search(r'[a-z]', v):
            raise ValueError('Debe tener al menos una minúscula')
        if not re.search(r'\d', v):
            raise ValueError('Debe tener al menos un número')
        if ' ' in v:
            raise ValueError('No puede contener espacios')
        return v

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"