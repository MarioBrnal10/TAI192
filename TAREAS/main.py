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