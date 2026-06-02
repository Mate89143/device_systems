from fastapi import FastAPI, Request, Response
from app.routes.user_routes import router as user_router

app = FastAPI(
    title="device_systems API",
    description="API REST para gestión de usuarios (CRUD completo, manejo de errores, DI)",
    version="2.0.0",
    contact={
        "name": "Tu Nombre",
        "email": "tuemail@ejemplo.com",
    },
    license_info={
        "name": "MIT",
    },
    docs_url="/docs",
    redoc_url="/redoc"
)

# Incluir rutas
app.include_router(user_router)

# Middleware para cabeceras personalizadas (opcional, ya las puso antes)
@app.middleware("http")
async def add_custom_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "2.0.0"
    return response

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Bienvenido a device_systems API v2.0"}