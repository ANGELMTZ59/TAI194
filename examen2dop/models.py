from pydantic import BaseModel, Field

class modelAuto(BaseModel):
    id: int = Field(..., gt=0, description="El ID siempre debe ser positivo")
    modelo: str = Field(..., min_length=1, max_length=25, description="modelo debe tener maximo 25 caracteres")
    año: int = Field(...,gt=0, description="el año debe tener 4 digitos", ge=1000, le=9999)
    placa: str = Field(..., min_length=1, max_length=10, description="La placa solo debe tener 10 caracteres maximos")

