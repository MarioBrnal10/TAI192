from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title='Mi Primer API 192',
    description='Bernal',
    version='1.0.1'
)

usuarios = [
    {"id": 1, "Nombre": "Mario", "Edad": 21},
    {"id": 2, "Nombre": "Gelipe", "Edad": 20},
    {"id": 3, "Nombre": "Alonso", "Edad": 22},
    {"id": 4, "Nombre": "Mariano", "Edad": 23}
]


# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

# Endpoint Colsulta Usuarios
@app.get('/todosUsuarios', tags=['Operaciones CRUD'])
def leerUsuarios():
    return {"Los Usuarios Registrados Son": usuarios}

#endpoint Agregar nuevos
@app.post('/usuario/', tags=['Operaciones CRUD'])
def agregarUsuario(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El id ya Existe")
    usuarios.append(usuario)
    return usuario

# Endpoint Actualizar Usuarios
@app.put('/usuario/{id}', tags=['Operaciones CRUD'])
def actualizarUsuario(id:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")
            
#endpoint Eliminar Usuarios
@app.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def eliminarUsuario(id:int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            raise HTTPException(status_code=400, detail="El Esuario Eliminado")
    return {"El id Ya no Existe"}