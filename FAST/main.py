from fastapi import FastAPI, HTTPException
from typing import Optional, List
from models import modeloUsuario

app = FastAPI(
    title='Mi Primer API 192',
    description='Bernal',
    version='1.0.1'
)



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

# Endpoint CONSULTA TODOS
@app.get("/todoUsuarios", response_model=List[modeloUsuario], tags=["Operaciones CRUD"])
def leer_usuarios():
    return usuarios

#endpoint Agregar nuevos
@app.post('/usuario/', response_model= modeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuario(usuario: modeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El id ya Existe")
    usuarios.append(usuario)
    return usuario

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


