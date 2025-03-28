from fastapi import FastAPI
from DB.conexion import  engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth

app = FastAPI(
    title="Mi primera API",
    description="Angel Daniel Martinez Maqueda",
    version="1.0.1"
)
Base.metadata.create_all(bind=engine)
app.include_router(routerUsuario)
app.include_router(routerAuth)
