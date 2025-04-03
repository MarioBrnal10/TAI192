from fastapi import FastAPI 
from DB.conexion import engine, Base 
from routers.usuario import routerUsuario
from routers.auth import routerAuth
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(
    title='Mi Primer API 192',
    description='Bernal',
    version='1.0.1'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)




Base.metadata.create_all(bind=engine)



# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

app.include_router(routerUsuario)
app.include_router(routerAuth)