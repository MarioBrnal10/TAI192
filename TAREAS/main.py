from fastapi import FastAPI, HTTPException
from typing import Optional


app = FastAPI(
    title='API Repaso S-192',
    description='Creado Por Mario Bernal',
    version='1.0.1'
)

tareas = [
  {
    "id": 1,
    "titulo": "Practica 1",
    "descripcion": "Repasar los apuntes de TAI",
    "vencimiento": "14-02-24",
    "Estado": "completada"
  },
  {
    "id": 2,
    "titulo": "Practica 2",
    "descripcion": "Entrenar 30 minutos de cardio",
    "vencimiento": "15-02-24",
    "Estado": "no completada"
  },
  {
    "id": 3,
    "titulo": "Practica 3",
    "descripcion": "Avanzar 50 páginas de la novela",
    "vencimiento": "20-02-24",
    "Estado": "completada"
  },
  {
    "id": 4,
    "titulo": "Practica De Repaso",
    "descripcion": "Leche, pan, huevos, frutas y verduras",
    "vencimiento": "12-02-24",
    "Estado": "no completada"
  },
  {
    "id": 5,
    "titulo": "Terminar el proyecto de programación",
    "descripcion": "Finalizar la última funcionalidad y probar",
    "vencimiento": "25-02-24",
    "Estado": "completada"
  },
  {
    "id": 6,
    "titulo": "Desarrollar  Forntend ",
    "descripcion": "Ponerse al día con Juan",
    "vencimiento": "18-02-24",
    "Estado": "no completada"
  },
  {
    "id": 7,
    "titulo": "Instalar Una Maquina Virtual",
    "descripcion": "Ordenar la habitación y limpiar el escritorio",
    "vencimiento": "22-02-24",
    "Estado": "completada"
  },
  {
    "id": 8,
    "titulo": "Hacer la Particion de Disco",
    "descripcion": "Agregar últimos proyectos y experiencia",
    "vencimiento": "28-02-24",
    "Estado": "no completada"
  }
]

# Endpoint home
@app.get('/', tags=['API para la Gestion de Tareas'])
def home():
    return {'Tareas': 'UPQ'}

# Endpoint Para ver Tareas
@app.get('/tareas', tags=['Tareas'])
def ver_tarea():
  return {"Todas Las Tareas Son": tareas}

# Endpoint para obtener una tarea en especifico
@app.get('/tareas/{tarea_id}', tags=['Tareas'])
def consultarTarea(tarea_id: int):
    for tar in tareas:
        if tar["id"] == tarea_id:
            return {"La Tarea Con Ese Id es": tar}
    return {"Mensaje": f"No Hay ninguna Tarea Con Ese Id: {tarea_id}"}
  

# Endopint para  Crear Una Nueva Tarea4
@app.post('/tareas/', tags=['Tareas'])
def agregarTarea(tarea:dict):
    for tar in tareas:
        if tar["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="Ya Existe Una Tarea Con Ese Id")
    tareas.append(tarea)
    return tarea
  
# Endpoint Actualizar Tarea
@app.put('/tarea/{id}', tags=['Tareas'])
def actualizarTarea(id: int, tareaActualizada:dict):
  for index, tar in enumerate(tareas):
    if tar["id"] == id:
      tareas[index].update(tareaActualizada)
      return tareas[index]
  raise HTTPException(status_code=400, detail="No Existe Una Tarea Con Ese Id")

#Endpoint Eliminar tarea
@app.delete('/tarea/{id}', tags=['Tareas'])
def eliminarTarea(id: int):
      for tar in tareas:
        if tar["id"] == id:
            tareas.remove(tar)
            raise HTTPException(status_code=400, detail="Tarea Eliminada")
      return {"La Tarea Ya no Exixte"}
