from pydantic import BaseModel, Field
from typing import Optional

class FincaBase(BaseModel):

    nombre: str = Field(min_length=2, max_length=30)
    longitud: float 
    latitud: float
    id_usuario: int
    estado: bool

class FincaCreate(FincaBase):
    estado: bool

class FincaUpdate(BaseModel):
    nombre: Optional[str] = Field(default=None, min_length=3, max_length=80)
    longitud: Optional[float] = Field(default=None)
    longitud: Optional[float] = Field(default=None)
    
class FincaEstado(BaseModel):
    estado: Optional[bool] = None

class FincaOut(FincaBase):
    id_finca: int
    nombre_usuario: str

