# device_systems

## Descripción de la aplicación

"device_systems" permite gestionar usuarios de un sistema interno. Cada usuario tiene los siguientes campos:

| Campo       | Tipo    | Requerido | Validación / Regla                               |
|-------------|---------|-----------|--------------------------------------------------|
| "id"        | integer | automático| Se asigna secuencialmente                        |
| "name"      | string  | sí        | mínimo 3 caracteres                              |
| "email"     | string  | sí        | formato válido (debe contener "@" y un dominio)  |
| "role"      | string  | sí        | solo "admin", "support" o "user" (Enum)          |
| "is_active" | boolean | sí        | por defecto "true"                              |

### Características principales

- Listado de usuarios con filtros opcionales por rol y estado activo/inactivo.
- Consulta de un usuario por su ID mediante *path parameter*.
- Registro de nuevos usuarios con validaciones automáticas (Pydantic) y control de email duplicado.
- Respuestas estructuradas usando response models.
- Cabeceras HTTP personalizadas: "X-App-Name" y "X-API-Version".
- Documentación interactiva automática: Swagger UI y ReDoc.

## Creación de entorno y virtual e Instalación de dependencias

Se utilizó GitHub Codespaces con Python 3.12. Los pasos se muestran en la siguiente captura:

![Creación de entorno virtual e instalación de dependencias](/images/Creación%20de%20entorno%20virtual%20e%20instalación%20de%20dependencias.png)

1. Crear entorno virtual:  

python -m venv venv

2. Activar el entorno virtual:

source venv/bin/activate

3. Crear el archivo requirements.txt en la raíz del proyecto con:

fastapi==0.115.0
uvicorn[standard]==0.31.0

4. Instalar dependencias:

pip install -r requirements.txt

## Verificación de paquetes instalados

![Lista](/images/Lista.png)

## Ejecución del servidor

Con el entorno virtual activado, en la raíz del proyecto se ejecuta:

uvicorn app.main:app --reload

El servidor se levanta en la URL asignada por Codespaces.
La ruta raíz (/) responde con un mensaje de bienvenida:

![Localhost](/images/Localhost.png)

La documentación interactiva está disponible en:

https://urban-doodle-pj9rqj4xvg6wf7xjx-8000.app.github.dev/docs#/users

Así se ve la URL según el nombre de mi CodeSpace.

![Localhost2](/images/Localhost%202.png)

## Tabla de endpoints

| Método | Endpoint                     | Descripción                                   | Parámetros                                      |
|--------|------------------------------|-----------------------------------------------|-------------------------------------------------|
| GET    | "/users"                     | Listar usuarios (con filtros opcionales)      | "role" (query, string), "is_active" (query, boolean) |
| GET    | "/users/{user_id}"           | Obtener un usuario por su ID                  | "user_id" (path, entero ≥ 1)                   |
| POST   | "/users"                     | Crear un nuevo usuario                        | Body JSON (modelo "UserCreate")                |
| GET    | "/"                          | Mensaje de bienvenida                         | -                                               |

# Capturas del SWAGGER UI

## 1. 
![Localhost](/images/Localhost.png)

Respuesta de la ruta raíz – API activa

## 2. 
![Localhost2](/images/Localhost%202.png)

Vista general de todos los endpoints en Swagger UI

## 3. 
![Localhost2.1](/images/Localhost%202.1.png)

Esquemas de datos documentados automáticamente

## 4. 
![Get users](/images/Get%20users.png)

Parámetros de consulta (role, is_active) para GET /users

## 5. 
![Get users 2](/images/Get%20users%202.png)

Ejecución de GET /users con filtros, respuesta 200 y cabeceras

## 6. 
![Get users 3](/images/Get%20users%203.png)

Esquema de respuesta exitosa para GET /users (documentación)

## 7. 
![Get users id](/images/Get%20users%20id.png)

Parámetro path user_id con validación minimum: 1

## 8. 
![Get users id 2](/images/Get%20users%20id%202.png)

Respuesta 404 al buscar un ID inexistente

## 9. 
![Get users id 3](/images/Get%20users%20id%203.png)

Esquema de respuesta exitosa para GET /users/{user_id}

## 10. 
![Post users](/images/Post%20users.png)

Cuerpo de la petición POST /users en Swagger

## 11. 
![Post users 2](/images/Post%20users%202.png)

Error 422 por email inválido – detalle de validación

## 12. 
![Post users 3](/images/Post%20users%203.png)

Encabezados de respuesta incluyendo cabeceras personalizadas

## 13. 
![Post users 4](/images/Post%20users%204.png)

Esquema de respuesta exitosa (201) para POST

# Capturas adicionales

## 14. 
![Instalación de Pydantic](/images/Instalación%20de%20Pydantic.png)

Verificación de Pydantic instalado

## 15. 
![Instalación de Uvicorn](/images/Instalando%20uvicorn.png)

Confirmación de instalación de Uvicorn

## 16. 
![Visualización de esquemas](/images/Schemas.png)

## 17. 
![Visualización de esquemas](/images/Schemas%202.png)



# device_systems (2 de junio de 2026)

## Nombre del proyecto

device_systems – API REST para gestión de usuarios.

## Descripción de la API

API desarrollada con FastAPI que permite realizar operaciones CRUD completas sobre usuarios de un sistema interno.  
Incluye validaciones automáticas, manejo profesional de errores, códigos de estado HTTP apropiados, Dependency Injection y documentación interactiva generada automáticamente con Swagger UI y ReDoc.

## Tecnologías utilizadas

- Python 3.12+
- FastAPI – framework web moderno
- Pydantic v2 – validación de datos
- Uvicorn – servidor ASGI
- Git / GitHub – control de versiones

## Instalación de dependencias

## Clonar el repositorio

git clone https://github.com/tu-usuario/device_systems.git
cd device_systems

o simplemente habilitar codespace.

## Crear y activar entorno virtual

- python -m venv venv
- source venv/bin/activate   # Linux/macOS
- venv\Scripts\activate    # Windows

## Instalar dependencias

pip install -r requirements.txt

## Contenido de requirements.txt

fastapi==0.115.0

uvicorn[standard]==0.31.0

## Comando para ejecutar el servidor

uvicorn app.main:app --reload

Accede a la documentación interactiva en:

- Swagger UI: http://localhost:8000/docs

## Tabla de endpoints (CRUD completo)

| Método | Endpoint               | Descripción                          | Códigos de estado principales |
|--------|------------------------|--------------------------------------|-------------------------------|
| GET    | "/users"               | Listar usuarios (filtros opcionales) | 200 OK                        |
| GET    | "/users/{user_id}"     | Obtener usuario por ID               | 200 OK, 404 Not Found         |
| POST   | "/users"               | Crear nuevo usuario                  | 201 Created, 400, 422         |
| PUT    | "/users/{user_id}"     | Actualización completa               | 200 OK, 404, 400              |
| PATCH  | "/users/{user_id}"     | Actualización parcial                | 200 OK, 400, 404              |
| DELETE | "/users/{user_id}"     | Eliminar usuario                     | 204 No Content, 404           |

## Ejemplos de peticiones y respuestas

### POST /users – Crear usuario

```json:

{
  "name": "Ana Martínez",
  "email": "ana@example.com",
  "role": "admin",
  "is_active": true
}

```
# 201 (Created)

```json

{
  "id": 1,
  "name": "Ana Martínez",
  "email": "ana@example.com",
  "role": "admin",
  "is_active": true
}

```

# GET /users/1 – Usuario no encontrado. Respuesta (404):

```json

{
  "detail": "Usuario no encontrado"
}

```

## Códigos de estado de uso

| Código | Nombre                    | Cuándo se usa                                               |
|--------|---------------------------|-------------------------------------------------------------|
| 200    | OK                        | GET, PUT, PATCH exitosos                                    |
| 201    | Created                   | POST exitoso (usuario creado)                               |
| 204    | No Content                | DELETE exitoso                                              |
| 400    | Bad Request               | Email duplicado, PATCH sin datos, ID inválido               |
| 404    | Not Found                 | Usuario no encontrado                                       |
| 422    | Unprocessable Entity      | Datos no válidos (validación de Pydantic, ej. email sin @)  |

# Capturas del SWAGGER UI

## 1. GET /users – Parámetros de filtro (role, is_active)
![Get users nuevo](/images/Get%20users%20nuevo.png)

## 2. GET con filtros – Respuesta 200 (vacía) y cabeceras
![Get users nuevo 2](/images/Get%20users%20nuevo%202.png)

## 3. GET /{user_id} – Parámetro path ID
![Get users id nuevo](/images/Get%20users%20id%20nuevo.png)

## 4. GET /1 – Error 404 (usuario no encontrado)
![Get users id nuevo 2](/images/Get%20users%20id%20nuevo%202.png)

## 5. POST – Cuerpo del request (campos obligatorios)
![Post users nuevo](/images/Post%20users%20nuevo.png)

## 6. POST – Respuesta exitosa (no disponible)
![Post users nuevo 2](/images/Post%20users%20nuevo%202.png)

## 7. POST – Cabeceras de respuesta (x-api-version, x-app-name)
![Post users nuevo 3](/images/Post%20users%20nuevo%203.png)

## 8. PUT – Actualización completa (todos los campos)
![Put users nuevo](/images/Put%20users%20nuevo.png)

## 9. PUT /1 – Error 404 (usuario no encontrado)
![Put users nuevo 2](/images/Put%20users%20nuevo%202.png)

## 10. PUT – Cabeceras de respuesta
![Put users nuevo 3](/images/Put%20users%20nuevo%203.png)

## 11. PATCH – Actualización parcial (campos opcionales)
![Patch users nuevo](/images/Patch%20users%20nuevo.png)

## 12. PATCH /1 – Error 404 (usuario no encontrado)
![Patch users nuevo 2](/images/Patch%20users%20nuevo%202.png)

## 13. PATCH – Cabeceras de respuesta
![Patch users nuevo 3](/images/Patch%20users%20nuevo%203.png)

## 14. DELETE – Formulario con parámetro ID
![Delete users nuevo](/images/Delete%20users%20nuevo.png)

## 15. DELETE /0 – Error 404 (usuario no encontrado)
![Delete users nuevo 2](/images/Delete%20users%20nuevo%202.png)

## 16. Vista general de todos los endpoints en Swagger UI
![Endpoint](/images/Users.png)

## Explicación del uso de Depends() (Dependency Injection)

En el proyecto se crearon dependencias reutilizables dentro de "app/dependencies/user_dependencies.py". 

### Ejemplo: get_user_by_id

Esta función se encarga de buscar un usuario en la base de datos simulada (users_db) por su ID. Si el usuario existe, lo retorna. Si no, lanza una excepción #HTTPException# con código "404" y el mensaje "Usuario no encontrado".

```python:

def get_user_by_id(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

```

## Manejo de errores implementado

Se utiliza HTTPException de FastAPI en app/services/user_service.py para controlar:

404 – Cuando el usuario no existe (función get_user_or_404).

400 – Email duplicado al crear o actualizar, o PATCH sin campos.

422 – Automático de Pydantic (email sin @, nombre muy corto, rol inválido).

ejemplo: 
- raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Link video:
https://youtu.be/-feVSxmW44Q



# device_systems (9 de junio de 2026)

## Nombre del proyecto

device_systems – API REST para gestión de usuarios.

## Descripción de la API

Este proyecto representa la evolución de la API `device_systems` hacia una versión profesional con **persistencia real de datos**. Anteriormente los usuarios se almacenaban en listas en memoria; ahora se guardan en una base de datos **SQLite** mediante **SQLAlchemy**. Se implementa el CRUD completo (crear, leer, actualizar, eliminar), validaciones con Pydantic, constraints a nivel de base de datos, manejo de errores y documentación automática con Swagger UI. Esta versión demuestra cómo construir una API REST robusta y preparada para entornos de producción.

## Captura de la estructura del proyecto

## Estructura del proyecto
![Estructura del proyecto](/images/Estructura%20carpetas.png)

## Capturas

## Base de datos generada
![Base de datos generada](/images/Base%20de%20datos%20generada.png)

## SWAGGER UI

## Get users
![Get users](/images/Get%20users%20new.png)

![Get users](/images/Get%20users%20new%202.png)

## Get users id
![Get users id](/images/Get%20users%20id%20new.png)

![Get users id](/images/Get%20users%20id%20new%202.png)

## Post users
![Post users](/images/Post%20users%20new.png)

![Post users](/images/Post%20users%20new%202.png)

## Put users
![Put users](/images/Put%20users%20new.png)

![Put users](/images/Put%20users%20new%202.png)

## Delete users
![Delete users](/images/Delete%20users%20new.png)

![Delete users](/images/Delete%20users%20new%202.png)

## Diferencia entre modelo SQLAlchemy y schema Pydantic

Modelo SQLAlchemy (user_model.py): define la tabla en la BD. Usa Column, tipos SQL, restricciones (nullable=False, unique=True). No se expone a la API.

Schema Pydantic (user_schema.py): define la estructura de entrada/salida de la API. Usa BaseModel, validaciones (Field, EmailStr). Sí se expone y puede ocultar campos sensibles.

Conversión: FastAPI convierte automáticamente modelo → schema con response_model y from_attributes=True.
Por qué separarlos: seguridad (no exponer password_hash), flexibilidad (diferentes vistas) y validación clara.

## Reflexión sobre la persistencia en una API

Sin persistencia (listas en memoria): los datos se pierden al reiniciar el servidor.
Con persistencia (SQLAlchemy + SQLite/PostgreSQL): los datos permanecen, se pueden compartir entre instancias y se aplican constraints de integridad (UNIQUE, NOT NULL).

Además, usar un ORM evita SQL crudo, previene inyecciones, maneja transacciones y permite migraciones. En conjunto con FastAPI y Pydantic, se obtiene una API robusta y lista para producción.

# Link video:
https://youtu.be/WgzBKx8oPEU



# device_systems (18 de junio de 2026)

## Nombre del proyecto

device_systems – Alembic

## Capturas de pantalla

## Ejecución de alembic init
![Alembic init](/images/Instalación%20de%20alembic.png)

## Migración con alembic revision --autogenerate
![Migración alembic](/images/Migración%20con%20alembic%20revision%20--autogenerate.png)

## Migración con alembic upgrade head
![Migración](/images/Migración%20con%20alembic%20upgrade%20head.png)

## Estructura de tablas generadas
![Tablas](/images/Historial%20de%20tablas.png)

## Iniciando alembic
![Inicializar alembic](/images/Iniciando%20alembic.png)

## SWAGGER UI
![SWAGGER UI](/images/SWAGGER%20Users.png)
![SWAGGER UI](/images/SWAGGER%20Devices.png)
![SWAGGER UI](/images/SWAGGER%20Loans.png)

## Creación de usuario, dispositivo y préstamo.

### Usuarios
![Usuario](/images/Post%20users%20new%201.png)
![Usuario](/images/Post%20users%20new%201.1.png)

### Dispositivos
![Dispositivo](/images/Post%20devices.png)
![Dispositivo](/images/Post%20devices%202.png)

### Préstamos
![Préstamo](/images/Post%20loans.png)
![Préstamo](/images/Post%20loans%202.png)

## Consultas con joins

### Consulta por detalles
![Details](/images/Get%20loans%20details.png)
![Details](/images/Get%20loans%20details%202.png)

### Estado del préstamo
![Loans](/images/Get%20loans.png)
![Loans](/images/Get%20loans%202.png)

### Estado del dispositivo
![Devices](/images/Get%20devices.png)
![Devices](/images/Get%20devices%202.png)

### Detalles del préstamo
![Loans details](/images/Get%20loans%20new.png)
![Loand details](/images/Get%20loans%20new%202.png)

### Realización del préstamo
![Returned](/images/Patch%20loans.png)
![Returned](/images/Patch%20loans%202.png)

## Reflexión sobre la importancia de migraciones, relaciones y consultas avanzadas

La evolución de "device_systems" hacia un sistema con usuarios, dispositivos y préstamos se sostiene en tres pilares:

Migraciones con Alembic: Permiten versionar y aplicar cambios en la base de datos de forma controlada y reversible, garantizando consistencia entre entornos.

Relaciones entre modelos: Con "ForeignKey" y "relationship()" modelamos el dominio real: un usuario tiene préstamos, un préstamo involucra un dispositivo. Esto mantiene la integridad de los datos y hace el código más limpio.

Consultas con joins: Con "join()" obtenemos información combinada de varias tablas en una sola consulta, haciendo la API más rápida y eficiente.

Estos conceptos transforman una API básica en un sistema robusto y preparado para producción, demostrando el poder de FastAPI, SQLAlchemy y Alembic trabajando juntos.

# Link video:
https://youtu.be/Us7q0hxwcFw



# device_systems (23 de junio de 2026)

## Nombre del proyecto

device_systems – Security

## Capturas de pantalla

## Captura de la estructura del proyecto
![Carpetas](/images/Estructura%20de%20carpetas.png)

## Captura de migración Alembic aplicada
![Migración](/images/Migración%20con%20alembic.png)
![Migración](/images/Migración%20con%20alembic%201.png)

## Captura del registro de usuario
![Registro](/images/Post%20auth%20register.png)
![Registro](/images/Post%20auth%20register%201.png)

## Captura del login y token generado
![Token](/images/Post%20auth%20login.png)
![Token](/images/Post%20auth%20login%201.png)

## Captura de /auth/me
![Me](/images/Get%20auth%20me.png)

## Captura de acceso sin token
![Sin token](/images/Get%20auth%20me%20sin%20token.png)

## Captura de acceso con token
![Con token](/images/Get%20auth%20me%20con%20token.png)

## Captura de acceso con rol no permitido
![Rol no permitido](/images/Post%20devices%20rol.png)
![Rol no permitido](/images/Post%20devices%20rol%201.png)

## Captura de Swagger/OpenAPI con OAuth2
![OAuth2](/images/Authorize.png)
![OAuth2](/images/Authorize%20logrado.png)

## Captura de cabeceras del middleware
![Cabecera](/images/Get%20users%20rol.png)
![Cabecera](/images/Get%20users%20rol%201.png)
![Cabecera](/images/Get%20users%20rol%202.png)

## Captura de prueba de rate limiting
![Limiting](/images/Rate%20limit.png)
![Limiting](/images/Rate%20limit%201.png)

## Tabla de códigos de estado HTTP usados

| Código | Significado           | Uso en la API                                              |
|--------|-----------------------|------------------------------------------------------------|
| 200    | OK                    | Respuestas exitosas (GET, PUT, PATCH)                      |
| 201    | Created               | POST (registro, creación)                                  |
| 204    | No Content            | DELETE exitoso                                             |
| 400    | Bad Request           | Datos inválidos, email duplicado                           |
| 401    | Unauthorized          | Token ausente, inválido o expirado                         |
| 403    | Forbidden             | Rol insuficiente para la operación                         |
| 404    | Not Found             | Recurso no encontrado                                      |
| 422    | Unprocessable Entity  | Validación de Pydantic fallida                             |
| 429    | Too Many Requests     | Límite de rate limiting excedido                           |

## Tecnologías utilizadas

Python 3.13
FastAPI – framework web
SQLAlchemy – ORM
Alembic – migraciones
SQLite – base de datos (desarrollo)
Pydantic v2 – validación de datos
JWT (python-jose) – autenticación
bcrypt – hash de contraseñas
slowapi – rate limiting
Uvicorn – servidor ASGI

## Instalación y ejecución

# 1. Crear y activar entorno virtual
python -m venv env
source env/bin/activate  # o env\Scripts\activate en Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar variables de entorno (.env)
# (ver .env.example)

# 4. Aplicar migraciones
alembic upgrade head

# 5. Ejecutar servidor
uvicorn app.main:app --reload

## Pruebas con Swagger

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## Explicación de CORS configurado

En app/main.py se configuró CORS para permitir que solo frontends autorizados consuman la API:

python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
- allow_origins: Solo los orígenes especificados pueden acceder.

- allow_credentials=True: Permite enviar tokens de autenticación.

- allow_methods=["*"]: Permite todos los métodos HTTP.

- allow_headers=["*"]: Permite todos los headers.

Con allow_credentials=True no se puede usar "*" en allow_origins por seguridad. Se deben especificar los dominios exactos para evitar accesos no autorizados.

## Reflexión final sobre la importancia de la seguridad en APIs REST

La seguridad en una API es fundamental. Este proyecto me enseñó que:

Hash de contraseñas con bcrypt es obligatorio para proteger datos sensibles.

JWT permite autenticación sin estado, ideal para escalar.

Roles controlan qué puede hacer cada usuario (autorización).

Middleware mejora trazabilidad con cabeceras como X-Request-ID.

CORS y rate limiting protegen contra accesos no autorizados y ataques.

Una API sin seguridad es vulnerable. FastAPI facilita implementar estas capas de protección, convirtiendo un proyecto simple en un sistema robusto y confiable.

# Link video:
https://youtu.be/UNQMdR39CDs

# Link video solución al anterior:
https://youtu.be/kIUh_wAPG5E