from fastapi import FastAPI, HTTPException
from typing import Optional # define para que los caracteres en las api sean opcionales o no
app = FastAPI(
    title="Mi primera API",
    description="Angel Daniel Martinez Maqueda",
    version="1.0.1"
)

@app.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FasAPI!"}

tareas={
    {"id":1, 
     "titulo":"Estudiar para el examen",
     "descripcion":"Repasar los apuntes de TAI",
     "vencimiento":"14-02-25",
     "estado":"completada"},
     {"id":2,
     "titulo":"Ir a trabajar jaja",
     "descripcion":"Tengo que ir a trabajar mañana",
     "vencimiento":"15-02-25",
     "estado":"no completada",
     }
}
