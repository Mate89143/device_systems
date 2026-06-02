# device_systems (Mayo 26 de 2026)

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

## 1. Respuesta de la ruta raíz – API activa
![Localhost](/images/Localhost.png)

## 2. Vista general de todos los endpoints en Swagger UI
![Localhost2](/images/Localhost%202.png)

## 3. Esquemas de datos documentados automáticamente
![Localhost2.1](/images/Localhost%202.1.png)

## 4. Parámetros de consulta (role, is_active) para GET /users
![Get users](/images/Get%20users.png)

## 5. Ejecución de GET /users con filtros, respuesta 200 y cabeceras
![Get users 2](/images/Get%20users%202.png)

## 6. Esquema de respuesta exitosa para GET /users (documentación)
![Get users 3](/images/Get%20users%203.png)

## 7. Parámetro path user_id con validación minimum: 1
![Get users id](/images/Get%20users%20id.png)

## 8. Respuesta 404 al buscar un ID inexistente
![Get users id 2](/images/Get%20users%20id%202.png)

## 9. Esquema de respuesta exitosa para GET /users/{user_id}
![Get users id 3](/images/Get%20users%20id%203.png)

## 10. Cuerpo de la petición POST /users en Swagger
![Post users](/images/Post%20users.png)

## 11. Error 422 por email inválido – detalle de validación
![Post users 2](/images/Post%20users%202.png)

## 12. Encabezados de respuesta incluyendo cabeceras personalizadas
![Post users 3](/images/Post%20users%203.png)

## 13. Esquema de respuesta exitosa (201) para POST
![Post users 4](/images/Post%20users%204.png)

# Capturas adicionales

## 14. Verificación de Pydantic instalado
![Instalación de Pydantic](/images/Instalación%20de%20Pydantic.png)

## 15. Confirmación de instalación de Uvicorn
![Instalación de Uvicorn](/images/Instalando%20uvicorn.png)

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

ejemplo: raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Link video:
https://youtu.be/-feVSxmW44Q
