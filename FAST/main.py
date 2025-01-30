from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return{"message": "!Bienvenido a FasAPI!"}



#Endopoint: promedio
@app.get("/promedio")
def promedio():
    return 10.5


#Endpoint con parametro obligatorio
@app.get("/usuario/{id}")
def consultausuario(id: int):
    return{"se encontro el usuario":{id}}