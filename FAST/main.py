from fastapi import FastAPI, HTTPException
from typing import Optional # define para que los caracteres en las api sean opcionales o no
app = FastAPI(
    title="Mi primera API",
    description="Angel Daniel Martinez Maqueda",
    version="1.0.1"
)
usuarios=[
    {"id":1, "nombre":"Angel", "edad":20},
    {"id":2, "nombre":"Daniel", "edad":20},
    {"id":3, "nombre":"Alfredo", "edad":21},
    {"id":4, "nombre":"Aaron", "edad":22},
]

@app.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FasAPI!"}



# Enpoint CONSULTA TODOS
@app.get("/todosUsuarios/", tags=['Operaciones CRUD'])
def leer():
    return { 'Usarios Registrados: ': usuarios}


#Endpoint de tipo POST
@app.post("/usuarios/", tags=['Operaciones CRUD'])
def guardar(usuario:dict):
    for usr in usuarios:
        if usr["id"]==usuario.get("id"):
         raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario)
    return usuario

#Endpoint para actualizar
@app.put("/usuarios/{id}", tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")