from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from modelsPydantics import modelUsuario
from DB.conexion import Session
from models.modelsDB import User


from fastapi import APIRouter

routerUsuario = APIRouter()

# Enpoint CONSULTA TODOS
@routerUsuario.get("/todosUsuarios", tags=['Operaciones CRUD'])
def leer():
    db=Session()
    try:
        consulta= db.query(User).all()
        return JSONResponse( content=jsonable_encoder(consulta))
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al guardar", "Error": str(e)})
    finally:
        db.close()




# Endpoint para registrar un nuevo usuario
@routerUsuario.post("/usuarios/", response_model=modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario: modelUsuario):
    db=Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"message": "Usuario Guardado", "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al guardar", "Error": str(e)})
    finally:
        db.close()



#Endpoint para buscar por id
@routerUsuario.get("/usuario/{id}", tags=['Operaciones CRUD'])
def leeruno(id:int):
    db=Session()
    try:
        consulta1= db.query(User).filter(User.id == id).first()

        if not consulta1:
            return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})
        
        return JSONResponse( content=jsonable_encoder(consulta1))
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al guardar", "Error": str(e)})
    finally:
        db.close()




#Endpoint para actualizar
@routerUsuario.put("/usuarios/{id}", response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id: int, usuarioActualizado: modelUsuario):
    db = Session()
    try:
        query = db.query(User).filter(User.id == id)
        if not query.first():
            return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})
        
        actualizar_info = usuarioActualizado.model_dump(exclude_unset=True)
        query.update(actualizar_info)
        db.commit()
        usuario_actualizado = db.query(User).filter(User.id == id).first()
        return JSONResponse(content=jsonable_encoder(usuario_actualizado))
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al actualizar", "Error": str(e)})
    finally:
        db.close()




#Endpoint para eliminar
@routerUsuario.delete("/usuarios/{id}", tags=['Operaciones CRUD'])
def eliminar(id:int):
    db = Session()
    try:
        query = db.query(User).filter(User.id == id)
        usuario_eliminado = query.first()
        if not usuario_eliminado:
            return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})
        db.delete(usuario_eliminado)
        db.commit()
        
        return JSONResponse(content=jsonable_encoder(usuario_eliminado))
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al eliminar", "Error": str(e)})
    finally:
        db.close()

