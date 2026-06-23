from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.dependencies.database_dependency import get_db
from app.auth.security import decode_access_token
from app.services.user_service import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Token inválido")
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    return user

def get_current_active_user(current_user = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return current_user

def require_admin(current_user = Depends(get_current_active_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Se requiere rol admin")
    return current_user

def require_admin_or_support(current_user = Depends(get_current_active_user)):
    if current_user.role not in ["admin", "support"]:
        raise HTTPException(status_code=403, detail="Se requiere rol admin o support")
    return current_user