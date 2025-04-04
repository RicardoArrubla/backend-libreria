# 📚 Miniproyecto - Biblioteca Tulua (FastAPI + HTML)

Este proyecto consiste en una **API RESTful desarrollada con FastAPI** que permite gestionar una biblioteca: agregar, ver, actualizar y eliminar libros. Incluye un **frontend sencillo en HTML** con estilo andino, y está **desplegado en la nube con Railway**.

---

## 🚀 ¿Qué hace este proyecto?

Implementa un sistema completo para administrar libros:

- Crear libros (`POST`)
- Listar libros (`GET`)
- Obtener libro por ID (`GET`)
- Actualizar libro (`PUT`)
- Eliminar libro (`DELETE`)
- Toda la API está documentada automáticamente en `/docs` (Swagger UI)

Incluye un **frontend visual** para interactuar con la API usando HTML + JavaScript.

---

## 🧱 Componentes del sistema

| Componente         | Descripción                                        |
| ------------------ | -------------------------------------------------- |
| `main.py`          | Backend con FastAPI y lógica CRUD                  |
| `index.html`       | Frontend simple en HTML/JS para probar visualmente |
| `requirements.txt` | Lista de dependencias (`fastapi`, `uvicorn`)       |

---

## 🛠️ Cómo ejecutar en local

### 🔧 Requisitos:

- Python 3.10 o superior
- Pip instalado

### 💻 Pasos:

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/backend-libreria.git
cd backend-libreria

# 2. Crear y activar entorno virtual (opcional pero recomendado)
python -m venv env
.\env\Scripts\activate   # En Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar servidor FastAPI
uvicorn main:app --reload

Abre en tu navegador: http://127.0.0.1:8000/docs

🖼️ Usar el frontend
Abre el archivo index.html con doble clic o usando Live Server en VS Code.

Asegúrate de que FastAPI esté corriendo en http://127.0.0.1:8000

Usa el formulario para agregar, ver, editar y eliminar libros.


```
