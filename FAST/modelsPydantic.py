from pydantic import BaseModel, Field, EmailStr

# Modelo de validaciones
class modeloUsuario(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="El nombre del usuario debe tener entre 3 y 50 caracteres")
    age: int = Field(..., gt=0, description="La edad del usuario debe ser positiva")
    email: str = Field(..., pattern="^[\w\.-]+@[\w\.-]+\.\w+$", examples=["mario@example.com"])

#Modelo de autenticación
class modeloAuth(BaseModel):
    email: EmailStr = Field(..., pattern="^[\w\.-]+@[\w\.-]+\.\w+$", examples=["example@gmail.com"])
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="La contraseña debe tener al menos 8 caracteres")
