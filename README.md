# BibliotecaApp

Este es un sistema de gestión de bibliotecas desarrollado con **Django**. El sistema permite gestionar bibliotecas, libros, usuarios y préstamos. A través de este sistema, los usuarios pueden realizar préstamos de libros y las bibliotecas pueden administrar su inventario de libros.

## Características

- **Gestión de Bibliotecas**: Crear y consultar bibliotecas.
- **Gestión de Libros**: Agregar, consultar, editar y eliminar libros de la base de datos.
- **Gestión de Usuarios**: Registrar y consultar usuarios.
- **Gestión de Préstamos**: Registrar préstamos de libros, marcar libros como devueltos.
- **Consultas por Biblioteca**: Listar los libros disponibles en una biblioteca.
- **Filtrar por Disponibilidad**: Filtrar libros prestados o disponibles.

## Tecnologías

- **Python 3.12.0**
- **Django 5.1.6**
- **SQLite**: Base de datos predeterminada (para desarrollo)
- **Django REST Framework** (opcional, si se utiliza para exposiciones de API)
- **JSON**: Para intercambiar datos entre el frontend y el backend

## Requisitos

Asegúrate de tener las siguientes herramientas instaladas en tu sistema:

- **Python 3**
- **pip**: El gestor de paquetes de Python

## Instalación

### 1. Clonar el repositorio

Primero, clona el repositorio de GitHub:

```bash
git clone https://github.com/tu-usuario/biblioteca-management.git
cd biblioteca-management
```

### 2. Crear un entorno virtual (opcional pero recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scriptsctivate
```

### 3. Instalar las dependencias

Instala las dependencias del proyecto con `pip`:

```bash
pip install -r requirements.txt
```

### 4. Migrar la base de datos

Realiza las migraciones de la base de datos para crear las tablas necesarias:

```bash
python manage.py makemigrations app
python manage.py migrate
```

### 5. Crear un superusuario (opcional)

Para poder acceder al panel de administración de Django, puedes crear un superusuario:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en la terminal para configurar el superusuario.

### 6. Ejecutar el servidor de desarrollo

Inicia el servidor de desarrollo con:

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`.

## API Endpoints

### Bibliotecas

- **GET** `/libraries`: Obtiene todas las bibliotecas registradas.
- **POST** `/libraries`: Crea una nueva biblioteca. Se debe enviar un cuerpo de solicitud JSON con los campos `name` y `location`.
- **GET** `/libraries/{library_id}`: Obtiene los detalles de una biblioteca específica por `id`.

### Libros

- **POST** `/books`: Crea un nuevo libro. Debes proporcionar los campos `isbn`, `title`, `genre`, `author`, `editorial`, `format`, `age_range`, y `library_id`.
- **GET** `/libraries/{library_id}/books`: Obtiene los libros de una biblioteca específica por `id`.
- **GET** `/books/{book_id}`: Obtiene los detalles de un libro específico por `id`.
- **PUT/PATCH** `/books/{book_id}`: Modifica un libro específico por `id`. Debes proporcionar los campos `isbn`, `title`, `genre`, `author`, `editorial`, `format` y `age_range` editados.
- **DELETE** `/books/{book_id}`: Elimina un libro específico por `id`.

### Usuarios

- **GET** `/users`: Obtiene todos los usuarios.
- **POST** `/users`: Registra un nuevo usuario. Se debe proporcionar `dni`, `email`, `telf_number`, `name`, `surname` y `birthdate`.
- **GET** `/users/{user_id}`: Obtiene los detalles de un usuario específico por `id`.

### Préstamos

- **GET** `/loans`: Obtiene todos los préstamos registrados.
- **POST** `/loans`: Crea un préstamo de libro. Se deben proporcionar `user_id` y `book_id`.
- **GET** `/users/{user_id}/loans`: Obtiene todos los préstamos de un usuario específico por `id`.
- **POST** `/loans/{loan_id}`: Marca un préstamo como devuelto.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Gracias por usar este sistema de gestión de biblioteca! 😊
