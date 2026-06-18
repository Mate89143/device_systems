from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from fastapi import HTTPException, status
from datetime import datetime
from app.models.loan_model import Loan
from app.models.user_model import User
from app.models.device_model import Device
from app.schemas.loan_schema import LoanCreate, LoanUpdate

def get_loan_by_id(db: Session, loan_id: int):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return loan

def get_all_loans(db: Session, status: str = None, user_id: int = None, device_id: int = None,
                  user_email: str = None, device_type: str = None):
    query = db.query(Loan)
    if status:
        query = query.filter(Loan.status == status)
    if user_id:
        query = query.filter(Loan.user_id == user_id)
    if device_id:
        query = query.filter(Loan.device_id == device_id)
    if user_email:
        query = query.join(User, Loan.user_id == User.id).filter(User.email == user_email)
    if device_type:
        query = query.join(Device, Loan.device_id == Device.id).filter(Device.device_type == device_type)
    return query.all()

def get_loans_with_details(db: Session, filters: dict = None):
    """Consulta con joins para obtener información enriquecida"""
    query = db.query(Loan).join(User).join(Device)
    # Aplicar filtros si vienen en el dict
    if filters:
        if "status" in filters:
            query = query.filter(Loan.status == filters["status"])
        if "user_id" in filters:
            query = query.filter(Loan.user_id == filters["user_id"])
        if "device_id" in filters:
            query = query.filter(Loan.device_id == filters["device_id"])
        if "user_email" in filters:
            query = query.filter(User.email == filters["user_email"])
        if "device_type" in filters:
            query = query.filter(Device.device_type == filters["device_type"])
        if "search" in filters:
            search = filters["search"]
            query = query.filter(
                or_(
                    User.name.ilike(f"%{search}%"),
                    User.email.ilike(f"%{search}%"),
                    Device.name.ilike(f"%{search}%"),
                    Device.serial_number.ilike(f"%{search}%")
                )
            )
    return query.all()

def create_loan(db: Session, loan_data: LoanCreate):
    # Verificar existencia de usuario y dispositivo
    user = db.query(User).filter(User.id == loan_data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    device = db.query(Device).filter(Device.id == loan_data.device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    if not device.is_available:
        raise HTTPException(status_code=409, detail="El dispositivo no está disponible")

    # Crear préstamo
    new_loan = Loan(
        user_id=loan_data.user_id,
        device_id=loan_data.device_id,
        status="active"
    )
    db.add(new_loan)

    # Marcar dispositivo como no disponible
    device.is_available = False
    try:
        db.commit()
        db.refresh(new_loan)
        return new_loan
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al crear el préstamo")

def return_device(db: Session, loan_id: int):
    loan = get_loan_by_id(db, loan_id)
    if loan.status != "active":
        raise HTTPException(status_code=409, detail="El préstamo ya fue devuelto o está vencido")
    # Marcar como devuelto
    loan.status = "returned"
    loan.return_date = datetime.utcnow()
    # Liberar dispositivo
    device = db.query(Device).filter(Device.id == loan.device_id).first()
    if device:
        device.is_available = True
    db.commit()
    db.refresh(loan)
    return loan