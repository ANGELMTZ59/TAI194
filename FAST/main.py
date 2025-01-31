from fastapi import FastAPI
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



#Endopoint: promedio
@app.get("/promedio", tags=['Mi calificacion TAI'])
def promedio():
    return 10.5


#Endpoint con parametro obligatorio
@app.get("/usuario/{id}", tags=['Endpoint parametro obligatorio'])
def consultausuario(id: int):
    return{"se encontro el usuario":{id}}


#Endpoint con parametro opcional
@app.get("/usuario2/", tags=['Endpoint parametro opcional'])
def consultausuario_opcional(id: Optional[int]=None):
    if id is not None:
        for usuario in usuarios: #usuario es la llave y usuarios es la lista
            if usuario["id"] == id:
                return {"mensaje": "usuario encontrado", "El usuario es: ": usuario}
        return {"mensaje":f"No se encontro el id {id}"} #f es para concatenar
    return{"mensaje": "No se proporciono un id"}



#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (id is None or usuario["id"] == id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}