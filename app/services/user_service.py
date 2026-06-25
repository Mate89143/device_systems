from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate

# ---------- READ ----------
def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_all_users(db: Session, role: str = None, is_active: bool = None):
    query = db.query(User)
    if role:
        query = query.filter(User.role == role)
    if is_active is not None:
        query = query.filter(User.is_active == is_active)
    return query.all()

# ---------- CREATE ----------
def create_user(db: Session, user_data: UserCreate):
    # Verificar email duplicado antes de intentar insertar
    if get_user_by_email(db, user_data.email):
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        role=user_data.role.value,
        is_active=user_data.is_active
    )
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error de integridad (email duplicado)")

# ---------- UPDATE ----------
def update_user_complete(db: Session, user_id: int, user_data: UserCreate):
    user = get_user_by_id(db, user_id)
    # Si cambia el email, verificar que no esté duplicado
    if user.email != user_data.email:
        if get_user_by_email(db, user_data.email):
            raise HTTPException(status_code=400, detail="El nuevo email ya está registrado")
    user.name = user_data.name
    user.email = user_data.email
    user.role = user_data.role.value
    user.is_active = user_data.is_active
    db.commit()
    db.refresh(user)
    return user

def update_user_partial(db: Session, user_id: int, user_data: UserUpdate):
    user = get_user_by_id(db, user_id)
    update_dict = user_data.model_dump(exclude_unset=True)
    if not update_dict:
        raise HTTPException(status_code=400, detail="No se enviaron campos para actualizar")
    if "email" in update_dict and user.email != update_dict["email"]:
        if get_user_by_email(db, update_dict["email"]):
            raise HTTPException(status_code=400, detail="El email ya está registrado")
    for field, value in update_dict.items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user

# ---------- DELETE ----------
def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    db.delete(user)
    db.commit()
    return True