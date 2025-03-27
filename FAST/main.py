from fastapi import FastAPI, HTTPException, Depends 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from modelsPydantic import modeloUsuario, modeloAuth
from genTokens import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base 
from models.modelsDB import User




app = FastAPI(
    title='Mi Primer API 192',
    description='Bernal',
    version='1.0.1'
)

Base.metadata.create_all(bind=engine)



usuarios = [
    {"id": 1, "nombre": "Mario", "edad": 21, "correo":"example@gmail.com"},
    {"id": 2, "nombre": "Gelipe", "edad": 20, "correo":"example2@gmail.com"},
    {"id": 3, "nombre": "Alonso", "edad": 22, "correo":"example3@gmail.com"},
    {"id": 4, "nombre": "Mariano", "edad": 23, "correo":"example4@gmail.com"}
]


# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

# Endpoint autenticación
@app.post('/auth',  tags=['Autentificación'])
def login(autorizacion: modeloAuth):
    if autorizacion.email == "mario@gmail.com" and autorizacion.passw == "123456789":
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return {"Aviso": "Credenciales incorrectas"}


# Endpoint CONSULTA TODOS
@app.get("/todoUsuarios", tags=["Operaciones CRUD"])
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
@app.get("/Usuarios/{id}", tags=["Operaciones CRUD"])
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
@app.post('/usuario/', response_model= modeloUsuario, tags=['Operaciones CRUD'])
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
@app.put('/usuario/{id}', response_model= modeloUsuario, tags=['Operaciones CRUD'])
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
@app.delete('/usuario/{id}', response_model= modeloUsuario, tags=['Operaciones CRUD'])
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
