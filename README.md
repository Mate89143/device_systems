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
