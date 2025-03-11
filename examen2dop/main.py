from fastapi import FastAPI, HTTPException
from models import modelAuto

app = FastAPI(
    title="Mi primera API",
    description="Angel Daniel Martinez Maqueda",
    version="1.0.1"
)


Autos=[
    {"id":1, 
     "modelo":"ejemoplomodelo",
     "año":"2025",
     "placa":"UKJ123"
    }
]




@app.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FasAPI!"}


#endpoint para consultar todo
@app.get("/Autos", tags=['Autos'])
def leer ():
    return {"Autos regristradas en la lista: ": Autos}



#endpoint para agregar un auto
@app.post("/agregarAuto/", response_model=modelAuto, tags=['Autos'])
def agregar(auto: modelAuto):
    for usr in Autos:
        if usr["id"]==auto.id:
            raise HTTPException(status_code=404, detail="Auto ya registrado")
    Autos.append(auto.model_dump())
    return auto



#endpoint para eliminar un Auto
@app.delete("/eliminarAuto/{id}", tags=['Autos'])
def eliminar(id:int):
    for index, auto in enumerate(Autos):
        if auto["id"]==id:
            Autos.pop(index)
            return { 'Autos Registradas: ': Autos}
    raise HTTPException(status_code=404, detail="Auto no encontrada")