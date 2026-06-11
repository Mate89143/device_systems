from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL de conexión a SQLite (archivo local)
DATABASE_URL = "sqlite:///./device_systems.db"

# Engine con configuración para SQLite (evita problemas de hilos)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para modelos
class Base(DeclarativeBase):
    pass

def create_tables():
    """Crea las tablas en la base de datos si no existen."""
    Base.metadata.create_all(bind=engine)