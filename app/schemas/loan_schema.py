from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.schemas.user_schema import UserResponse
from app.schemas.device_schema import DeviceResponse

class LoanCreate(BaseModel):
    user_id: int
    device_id: int
    # loan_date se asigna automáticamente, no se envía

class LoanUpdate(BaseModel):
    status: Optional[str] = Field(None, pattern="^(active|returned|overdue)$")
    return_date: Optional[datetime] = None

class LoanResponse(BaseModel):
    id: int
    user_id: int
    device_id: int
    loan_date: datetime
    return_date: Optional[datetime]
    status: str

    class Config:
        from_attributes = True

class LoanDetailResponse(BaseModel):
    """Respuesta enriquecida con datos del usuario y dispositivo"""
    id: int
    loan_date: datetime
    return_date: Optional[datetime]
    status: str
    user: UserResponse
    device: DeviceResponse