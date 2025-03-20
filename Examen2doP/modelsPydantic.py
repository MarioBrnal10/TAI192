from pydantic import BaseModel, Field

# Modelo para validar datos del conductor
class modeloCondurtores(BaseModel):
    Nombre: str = Field(..., min_length=3, description="Nombre del conductor")
    Tipo_Licencia: str = Field(..., min_length=1, description="Tipo de licencia")
    NoLicencia: str = Field(..., min_length=12, description="Numero de licencia") 
    