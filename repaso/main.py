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


