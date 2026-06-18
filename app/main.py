from fastapi import FastAPI
from app.routes import user_routes, device_routes, loan_routes
from app.database.connection import create_tables

app = FastAPI(
    title="device_systems API",
    description="API para gestión de usuarios, dispositivos y préstamos con SQLAlchemy, Alembic y relaciones",
    version="3.0.0",
    contact={"name": "Tu Nombre", "email": "tuemail@ejemplo.com"},
)

# Crear tablas al iniciar (si no existen)
create_tables()

# Incluir routers
app.include_router(user_routes.router)
app.include_router(device_routes.router)   # ← Agregar esta línea
app.include_router(loan_routes.router)     # ← Agregar esta línea

@app.get("/")
def root():
    return {"message": "Bienvenido a device_systems con base de datos, relaciones y migraciones"}