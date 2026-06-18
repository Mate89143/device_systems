from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.loan_schema import LoanCreate, LoanUpdate, LoanResponse, LoanDetailResponse
from app.services import loan_service
from app.dependencies.database_dependency import get_db
from app.models.user_model import User
from app.models.device_model import Device
from app.models.loan_model import Loan
from app.schemas.loan_schema import LoanDetailResponse

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.get("/", response_model=List[LoanResponse])
def get_loans(
    status: Optional[str] = Query(None, description="Filtrar por estado (active, returned, overdue)"),
    user_id: Optional[int] = Query(None, description="Filtrar por ID de usuario"),
    device_id: Optional[int] = Query(None, description="Filtrar por ID de dispositivo"),
    user_email: Optional[str] = Query(None, description="Filtrar por email del usuario"),
    device_type: Optional[str] = Query(None, description="Filtrar por tipo de dispositivo"),
    db: Session = Depends(get_db)
):
    return loan_service.get_all_loans(db, status, user_id, device_id, user_email, device_type)

@router.get("/details", response_model=List[LoanDetailResponse])
def get_loan_details(
    status: Optional[str] = Query(None),
    user_id: Optional[int] = Query(None),
    device_id: Optional[int] = Query(None),
    user_email: Optional[str] = Query(None),
    device_type: Optional[str] = Query(None),
    search: Optional[str] = Query(None, description="Búsqueda general en nombres y emails"),
    db: Session = Depends(get_db)
):
    filters = {}
    if status: filters["status"] = status
    if user_id: filters["user_id"] = user_id
    if device_id: filters["device_id"] = device_id
    if user_email: filters["user_email"] = user_email
    if device_type: filters["device_type"] = device_type
    if search: filters["search"] = search
    return loan_service.get_loans_with_details(db, filters)

@router.get("/{loan_id}", response_model=LoanDetailResponse)
def get_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = loan_service.get_loan_by_id(db, loan_id)
    result = db.query(Loan).join(User).join(Device).filter(Loan.id == loan_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return result

@router.post("/", response_model=LoanResponse, status_code=status.HTTP_201_CREATED)
def create_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    return loan_service.create_loan(db, loan)

@router.patch("/{loan_id}/return", response_model=LoanResponse)
def return_loan(loan_id: int, db: Session = Depends(get_db)):
    return loan_service.return_device(db, loan_id)