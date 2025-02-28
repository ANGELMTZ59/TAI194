from fastapi import FastAPI, HTTPException
from typing import Optional, List # define para que los caracteres en las api sean opcionales o no
from pydantic import BaseModel
from models import modelUsuario, modelAuth
from genToken import createToken

app = FastAPI(
    title="Mi primera API",
    description="Angel Daniel Martinez Maqueda",
    version="1.0.1"
)

usuarios=[
    {"id":1, "nombre":"Angel", "edad":20,"correo":"angelmaryinez1@gmail.com"},
    {"id":2, "nombre":"Daniel", "edad":20,"correo":"daniel@gmail.com"},
    {"id":3, "nombre":"Alfredo", "edad":21,"correo":"alfredo@gmail.com"},
    {"id":4, "nombre":"Aaron", "edad":22,"correo":"aaron@gmail.com"},
]

@app.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FasAPI!"}





#Endpoint de tipo POST para tokens
@app.post("/auth", tags=['Autentificacion'])
def auth(credenciales:modelAuth):
    if credenciales.mail == 'angel@gmail.com' and credenciales.passw == '12345678':
        token: str = createToken(credenciales.model_dump())
        print(token)
        return {"Aviso:": "Token Generado"}
    else:
        return{"Aviso:": "Credenciales incorrectas"}






# Enpoint CONSULTA TODOS
@app.get("/todosUsuarios/", response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def leer():
    return usuarios


#Endpoint de tipo POST
@app.post("/usuarios/", response_model= modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
    for usr in usuarios:
        if usr["id"]==usuario.id:
         raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario.dict())
    return usuario

#Endpoint para actualizar
@app.put("/usuarios/{id}",response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios[index]=usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")



#Endpoint para eliminar
@app.delete("/usuarios/{id}", tags=['Operaciones CRUD'])
def eliminar(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios.pop(index)
            return { 'Usuarios Registrados: ': usuarios}
    raise HTTPException(status_code=400, detail="El usuario no existe")


