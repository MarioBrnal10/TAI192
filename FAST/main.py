from fastapi import FastAPI, HTTPException, Depends 
from fastapi.responses import JSONResponse
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
@app.get("/todoUsuarios", dependencies=[Depends(BearerJWT())], response_model=List[modeloUsuario], tags=["Operaciones CRUD"])
def leer_usuarios():
    return usuarios

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

# Endpoint Actualizar Usuarios
@app.put('/usuario/{id}', response_model= modeloUsuario, tags=['Operaciones CRUD'])
def actualizarUsuario(id:int, usuarioActualizado:modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")
            
#endpoint Eliminar Usuarios
@app.delete('/usuario/{id}', response_model= modeloUsuario, tags=['Operaciones CRUD'])
def eliminarUsuario(id:int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            raise HTTPException(status_code=400, detail="El Esuario Eliminado")
    return {"El id Ya no Existe"}
