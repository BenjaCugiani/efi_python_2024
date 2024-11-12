# Efi Lucero Hugo, Pereyra Ariana, Cugiani Benjamin

Este proyecto está alojado en GitHub y se puede clonar y correr localmente siguiendo los pasos descritos a continuación.

Clonar y ejecutar el proyecto
# Clonar el proyecto
git clone #usar comando de git de hugo
cd efi_m_python_1

# Crear el entorno virtual
python3 -m venv env

# Activar el entorno virtual
source env/bin/activate

# Instalar requerimientos
pip install -r requirements.txt

# Correr el proyecto
flask run --reload

# Puntos finales de la API

A continuación se describen los principales endpoints de la API con ejemplos de solicitud y respuesta.

# Autenticación
# ATENCIÓN CREAR USUARIO ADMINISTRADOR CON FLASK SHELL
Obtener token de autenticación

Método: POST
Enpoint :localhost:5000/login
Cuerpo de la solicitud en el auth/basic:
{
    "username": "Admin",
    "password": "admin"
}
Ejemplo de respuesta:

{
    "Token": "<tu_token_de_autenticacion>"

}
# Creación de usuarios
Método: POST
Endpoint :localhost:5000/users
Pegar token de administrador en portador.
Cuerpo de la solicitud en el body/json:
{
    “usuario”: "Matias Lucero",
    “contrasenia”: "matilucero"
}
Ejemplo de respuesta:

{
  "Usuario Creado": "Matias Lucero"
}
# Ver lista de usuarios
Método: GET
Endpoint:localhost:5000/users
Pegar token de administrador en auth/bearer.
Pegar token de usuario en auth/bearer pero tendrá limitaciones al no ser admin.
Ejemplo de respuesta si sos admin:

  {
    "id": 10,
    "is_admin": null,
    "password_hash": "pbkdf2:sha256:600000$8aTB3wMS$70c0174c4ec2b496d07734c070ad3dcb512c7f0d7274f8ee944e01715fc3bb9d",
    "username": “Benjamin”
  }
Ejemplo de respuesta si no sos admin:

{
    "usuario”: "usuario 2"
  }
# CRUD en modelos de celulares
# Ver modelos
Método: GET
Endpoint:localhost:5000/modelo
Pegar token de administrador en auth/bearer.
Pegar token de usuario en auth/bearer pero tendrá limitaciones al no ser admin.
# Crear modelos
Método: POST
USUARIO SOLO ADMIN
Tiene que haber creado si o si un fabricante en la DB.
Endpoint:localhost:5000/modelos
Pegar ficha al portador.
Cuerpo de la solicitud en el body/json:
{
    "nombre": "iPhone 15",
    "activo": true,
    "marca_id": 1,
    "fabricante_id": 1
}
# Modificar modelos
Método: PUT
USUARIO SOLO ADMIN
Tiene que haber creado si o si un fabricante en la DB.
Endpoint:localhost:5000/modelos
Pegar ficha al portador.
Cuerpo de la solicitud en el body/json:
{
  "id": 1,
  "nombre": "Nuevo Nombre del Modelo",
  "activo": true,
  "marca_id": 2,
  "fabricante_id": 3
 }
# Eliminar modelos
Método: DELETE
USUARIO SOLO ADMIN
SE INACTIVA EL ID COPIANDO ESTA URL Y PONIENDO EL NUMERO DE ID QUE DESEAMOS DESACTIVAR.
Endpoint: AGREGAR LOCAL HOST 
Pegar ficha al portador.
Ejemplo de respuesta:

{
  "Mensaje": "Modelo marcado como inactivo correctamente."
}
# Otras vistas
Método: GET
Endpoint:localhost:5000/categorias
Endpoint :localhost:5000/equipos
Endpoint :localhost:5000/modelos