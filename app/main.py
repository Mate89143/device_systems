from fastapi import FastAPI
from app.routes import user_routes
from app.database.connection import create_tables

app = FastAPI(
    title="device_systems API",
    description="API con persistencia SQLAlchemy - CRUD completo de usuarios",
    version="3.0.0",
    contact={"name": "Tu Nombre", "email": "tuemail@ejemplo.com"},
)

# Crear tablas al iniciar (si no existen)
create_tables()

# Incluir rutas
app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a device_systems con base de datos"}