from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.device_schema import DeviceCreate, DeviceUpdate, DeviceResponse
from app.services import device_service
from app.dependencies.database_dependency import get_db
from app.models.user_model import User
from app.models.device_model import Device
from app.models.loan_model import Loan
from app.schemas.loan_schema import LoanDetailResponse

router = APIRouter(prefix="/devices", tags=["Devices"])

@router.get("/", response_model=List[DeviceResponse])
def get_devices(
    device_type: Optional[str] = Query(None, description="Filtrar por tipo de dispositivo"),
    is_available: Optional[bool] = Query(None, description="Filtrar por disponibilidad"),
    brand: Optional[str] = Query(None, description="Filtrar por marca (búsqueda parcial)"),
    search: Optional[str] = Query(None, description="Buscar en nombre o serial"),
    db: Session = Depends(get_db)
):
    return device_service.get_all_devices(db, device_type, is_available, brand, search)

@router.get("/{device_id}", response_model=DeviceResponse)
def get_device(device_id: int, db: Session = Depends(get_db)):
    return device_service.get_device_by_id(db, device_id)

@router.post("/", response_model=DeviceResponse, status_code=status.HTTP_201_CREATED)
def create_device(device: DeviceCreate, db: Session = Depends(get_db)):
    return device_service.create_device(db, device)

@router.put("/{device_id}", response_model=DeviceResponse)
def update_device(device_id: int, device: DeviceUpdate, db: Session = Depends(get_db)):
    return device_service.update_device_complete(db, device_id, device)

@router.patch("/{device_id}", response_model=DeviceResponse)
def patch_device(device_id: int, device: DeviceUpdate, db: Session = Depends(get_db)):
    return device_service.update_device_complete(db, device_id, device)

@router.delete("/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_device(device_id: int, db: Session = Depends(get_db)):
    device_service.delete_device(db, device_id)
    return None

@router.get("/{device_id}/loans", response_model=List[LoanDetailResponse])
def get_device_loans(device_id: int, db: Session = Depends(get_db)):
    device_service.get_device_by_id(db, device_id)
    loans = db.query(Loan).join(User).join(Device).filter(Loan.device_id == device_id).all()
    return loans