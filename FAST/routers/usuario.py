from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from modelsPydantic import modeloUsuario, modeloAuth
from genTokens import createToken
from middlewares import BearerJWT
from DB.conexion import Session 
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()


# Endpoint CONSULTA TODOS
@routerUsuario.get("/todoUsuarios", tags=["Operaciones CRUD"])
def leer_usuarios():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message": "Error al Consultar",
                            "Exception":str(e)})
    finally:
        db.close()
        
# Endpoint consulta por id
@routerUsuario.get("/Usuarios/{id}", tags=["Operaciones CRUD"])
def buscarUno(id:int):
    db = Session()
    try:
        consultaUno = db.query(User).filter(User.id == id).first()
        
        if not consultaUno:
            return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})
        return JSONResponse(content=jsonable_encoder(consultaUno))
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message": "Error al Consultar",
                            "Exception":str(e)})
    finally:
        db.close()

#endpoint Agregar nuevos
@routerUsuario.post('/usuario/', response_model= modeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuario(usuario: modeloUsuario):
    db = Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201,
                            content={"message": "Usuario Guardado",
                            "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message": "Error al Guardar al Usuario",
                            "Exception":str(e)})
    finally:
        db.close()

# Endpoint Actualizar Usuarios de la base de datos
@routerUsuario.put('/usuario/{id}', response_model= modeloUsuario, tags=['Operaciones CRUD'])
def actualizarUsuario(id:int, usuarioActualizado:modeloUsuario):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})
        db.query(User).filter(User.id == id).update(usuarioActualizado.model_dump())
        db.commit()
        return JSONResponse(content={"message": "Usuario Actualizado",
                                    "Usuario": usuarioActualizado.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message": "Error al Actualizar al Usuario",
                            "Exception":str(e)})
    finally:
        db.close()
#endpoint Eliminar Usuarios de la base de datos
@routerUsuario.delete('/usuario/{id}', response_model= modeloUsuario, tags=['Operaciones CRUD'])
def eliminarUsuario(id:int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})
        db.delete(consulta)
        db.commit()
        return JSONResponse(content={"message": "Usuario Eliminado"})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message": "Error al Eliminar al Usuario",
                            "Exception":str(e)})
    finally:
        db.close()