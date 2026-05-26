from fastapi import FastAPI, Request, Response
from app.routes.user_routes import router as user_router

app = FastAPI(
    title="device_systems API",
    description="API para administración de usuarios",
    version="1.0"
)

# Incluir rutas de usuarios
app.include_router(user_router, prefix="", tags=["users"])

# Middleware para agregar cabeceras personalizadas a todas las respuestas
@app.middleware("http")
async def add_custom_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"
    return response

# Endpoint raíz opcional
@app.get("/")
async def root():
    return {"message": "Bienvenido a device_systems API"}