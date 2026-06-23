from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.models.device_model import Device
from app.schemas.device_schema import DeviceCreate, DeviceUpdate

def get_device_by_id(db: Session, device_id: int):
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return device

def get_device_by_serial(db: Session, serial: str):
    return db.query(Device).filter(Device.serial_number == serial).first()

def get_all_devices(db: Session, device_type: str = None, is_available: bool = None, brand: str = None, search: str = None):
    query = db.query(Device)
    if device_type:
        query = query.filter(Device.device_type == device_type)
    if is_available is not None:
        query = query.filter(Device.is_available == is_available)
    if brand:
        query = query.filter(Device.brand.ilike(f"%{brand}%"))
    if search:
        query = query.filter(Device.name.ilike(f"%{search}%") | Device.serial_number.ilike(f"%{search}%"))
    return query.all()

def create_device(db: Session, device_data: DeviceCreate):
    if get_device_by_serial(db, device_data.serial_number):
        raise HTTPException(status_code=400, detail="El número de serie ya está registrado")
    new_device = Device(**device_data.model_dump())
    db.add(new_device)
    try:
        db.commit()
        db.refresh(new_device)
        return new_device
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error de integridad (serial duplicado)")

def update_device_complete(db: Session, device_id: int, device_data: DeviceUpdate):
    device = get_device_by_id(db, device_id)
    update_dict = device_data.model_dump(exclude_unset=True)
    if not update_dict:
        raise HTTPException(status_code=400, detail="No se enviaron campos para actualizar")
    if "serial_number" in update_dict:
        existing = get_device_by_serial(db, update_dict["serial_number"])
        if existing and existing.id != device_id:
            raise HTTPException(status_code=400, detail="El número de serie ya está registrado")
    for field, value in update_dict.items():
        setattr(device, field, value)
    db.commit()
    db.refresh(device)
    return device

def delete_device(db: Session, device_id: int):
    device = get_device_by_id(db, device_id)
    # Verificar si tiene préstamos activos
    if device.loans:
        active_loans = [loan for loan in device.loans if loan.status == "active"]
        if active_loans:
            raise HTTPException(status_code=409, detail="El dispositivo tiene préstamos activos, no se puede eliminar")
    db.delete(device)
    db.commit()
    return True