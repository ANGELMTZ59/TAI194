from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Mi primera API",
    description="Angel Daniel Martinez Maqueda",
    version="1.0.1"
)


tareas=[
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
]
@app.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FasAPI!"}


#endpoint para consultar todo
@app.get("/tareas", tags=['Tareas'])
def leer ():
    return {"tareas regristradas en la lista: ": tareas}

#endpoint de tarea por id
@app.get("/buscartarea", tags=['Tareas'])
def buscar(tarea_id: int):
    for tarea in tareas:
        if tarea["id"]==tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")



#endpoint para agregar una tarea
@app.post("/agregartarea/", tags=['Tareas'])
def agregar(tarea: dict):
    for usr in tareas:
        if usr["id"]==tarea["id"]:
            raise HTTPException(status_code=404, detail="Tarea ya existente")
    tareas.append(tarea)
    return tarea