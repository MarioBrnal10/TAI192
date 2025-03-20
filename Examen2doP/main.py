from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from modelsPydantic import modeloCondurtores

app = FastAPI(
    title="Examen 2do Parcial",
    
)

# conductores
conductores = [
    {"id": 1, "Nombre": "Mario", "Tipo_Licencia": "A", "NoLicencia": "12BN578CRI01"},
    {"id": 2, "Nombre": "Gelipe", "Tipo_Licencia": "B","NoLicencia": "12BN578CRI02"},
    {"id": 3, "Nombre": "Alonso", "Tipo_Licencia": "C", "NoLicencia": "12BN578CRI03"},
    {"id": 4, "Nombre": "Mariano", "Tipo_Licencia": "D", "NoLicencia": "12BN578CRI04"}
]

# endpoint para consultar conductor por No.Liciencia
@app.get("/conductores/{NoLicencia}", response_model=modeloCondurtores)
def get_conductor(NoLicencia: str):
    for conductor in conductores:
        if conductor["NoLicencia"] == NoLicencia:
            return conductor
    return {"message": "Conductor no encontrado"}


# endpoint para eliminar conductor por NoLicencia
@app.delete("/conductores/{NoLicencia}")
def eliminar_conductor(NoLicencia: str):
    for i, conductor in enumerate(conductores):
        if conductor["NoLicencia"] == NoLicencia:
            del conductores[i]
            return {"message": "Conductor eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Conductor no encontrado")
    
