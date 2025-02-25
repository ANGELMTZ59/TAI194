from pydantic import BaseModel, Field

class modelUsuario(BaseModel):
    id: int = Field(..., gt=0, description="El ID siempre debe ser positivo")
    nombre: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios, mínimo 1 y máximo 85 caracteres")
    edad: int = Field(..., ge=0, le=120, description="La edad debe ser entre 0 y 120")
    correo: str = Field(..., description="El correo debe ser un email válido", pattern=r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,6}$')
