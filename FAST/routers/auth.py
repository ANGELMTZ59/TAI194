from fastapi.responses import JSONResponse
from modelsPydantics import modelAuth
from genToken import createToken
from fastapi import APIRouter

routerAuth = APIRouter()



@routerAuth.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FasAPI!"}



#Endpoint de tipo POST para tokens
@routerAuth.post("/auth", tags=['Autentificacion'])
def auth(credenciales:modelAuth):
    if credenciales.mail == 'angel@gmail.com' and credenciales.passw == '12345678':
        token: str = createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return{"Aviso:": "Credenciales incorrectas"}