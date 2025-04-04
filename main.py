from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 👉 Middleware CORS para permitir conexión con el frontend (Live Server o archivo local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O usa ["http://localhost:5500"] si quieres restringirlo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos (Libro)
class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    disponible: bool = True

# Base de datos simulada (en memoria)
libros = []

# Crear un nuevo libro
@app.post("/items/")
def crear_libro(libro: Libro):
    libros.append(libro)
    return {"mensaje": "Libro agregado correctamente", "libro": libro}

# Obtener todos los libros
@app.get("/items/")
def obtener_libros():
    return libros

# Obtener un libro por ID
@app.get("/items/{id}")
def obtener_libro(id: int):
    for libro in libros:
        if libro.id == id:
            return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")

# Actualizar un libro por ID
@app.put("/items/{id}")
def actualizar_libro(id: int, libro_actualizado: Libro):
    for index, libro in enumerate(libros):
        if libro.id == id:
            libros[index] = libro_actualizado
            return {"mensaje": "Libro actualizado correctamente", "libro": libro_actualizado}
    raise HTTPException(status_code=404, detail="Libro no encontrado")

# Eliminar un libro por ID
@app.delete("/items/{id}")
def eliminar_libro(id: int):
    for index, libro in enumerate(libros):
        if libro.id == id:
            libros.pop(index)
            return {"mensaje": "Libro eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")

# Endpoint raíz (opcional)
@app.get("/")
def raiz():
    return {"mensaje": "¡Bienvenido a la API de la Biblioteca!"}
