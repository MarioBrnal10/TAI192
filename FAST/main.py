from fastapi import FastAPI
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

# Endpoint promedio
@app.get('/promedio', tags=['Mi Calificacion Parcial'])
def promedio():
    return 10

# Endpoint con parámetro obligatorio
@app.get('/usuario/{usuario_id}', tags=['Parametro Obligatorio'])
def consulta_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return {"Mensaje": "Usuario encontrado", "Usuario": usuario}
    return {"Mensaje": f"No se encontró el usuario con id: {usuario_id}"}

# Endpoint con parámetro opcional
@app.get('/usuario/', tags=['Parametro Opcional'])
def consulta_usuario_opcional(usuario_id: Optional[int] = None):
    if usuario_id is not None:
        for usuario in usuarios:
            if usuario["id"] == usuario_id:
                return {"Mensaje": "Usuario encontrado", "Usuario": usuario}
        return {"Mensaje": f"No se encontró el usuario con id: {usuario_id}"}
    else:
        return {'Mensaje': "No se proporcionó un id"}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios2(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["usuario_id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}