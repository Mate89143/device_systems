from fastapi import Depends, HTTPException, status
from app.services.user_service import get_user_or_404, check_email_duplicate
from app.schemas.user_schema import UserRole

def get_user_by_id(user_id: int):
    return get_user_or_404(user_id)

def validate_email_unique(email: str, user_id: int = None):
    check_email_duplicate(email, exclude_user_id=user_id)
    return email

def validate_role(role: UserRole):
    # Ya el Enum valida, pero podemos agregar lógica extra si se requiere
    return role