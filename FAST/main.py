from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import List
from models import modelUsuario, modelAuth
from genToken import createToken
from middlewares import BearerJWT

# Inicialización de la aplicación FastAPI
app = FastAPI(
    title="Mi primera API",
    description="Angel Daniel Martinez Maqueda",
    version="1.0.1"
)

# Lista de usuarios (simulación de base de datos)
usuarios = [
    {"id": 1, "nombre": "Angel", "edad": 20, "correo": "angelmaryinez1@gmail.com"},
    {"id": 2, "nombre": "Daniel", "edad": 20, "correo": "daniel@gmail.com"},
    {"id": 3, "nombre": "Alfredo", "edad": 21, "correo": "alfredo@gmail.com"},
    {"id": 4, "nombre": "Aaron", "edad": 22, "correo": "aaron@gmail.com"},
]

# Endpoint de inicio
@app.get("/", tags=['Inicio'])
def main():
    return {"message": "¡Bienvenido a FastAPI!"}

# Endpoint para generar token
@app.post("/auth", tags=['Autenticación'])
def auth(credenciales: modelAuth):
    if credenciales.mail == 'angel@gmail.com' and credenciales.passw == '12345678':
        token: str = createToken(credenciales.model_dump())  # Se usa model_dump() en lugar de dict()
        return JSONResponse(content=token)  
    else:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")









# Endpoint para obtener todos los usuarios (requiere token)
@app.get("/todosUsuarios/", response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def leer(token: dict = Depends(BearerJWT())):  # Ahora el token es un dict ya validado
    print("Token decodificado:", token)  # Para depuración
    return usuarios

# Endpoint para registrar un nuevo usuario
@app.post("/usuarios/", response_model=modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario: modelUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario.model_dump())  # Corrección de dict() a model_dump()
    return usuario

# Endpoint para actualizar un usuario
@app.put("/usuarios/{id}", response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id: int, usuarioActualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

# Endpoint para eliminar un usuario
@app.delete("/usuarios/{id}", tags=['Operaciones CRUD'])
def eliminar(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {'Usuarios Registrados': usuarios}
    raise HTTPException(status_code=400, detail="El usuario no existe")