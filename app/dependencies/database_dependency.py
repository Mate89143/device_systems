from app.database.connection import SessionLocal

def get_db():
    """Dependencia para inyectar sesión de BD en endpoints."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()