from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TareaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    prioridad: str = "media"
    fecha_vencimiento: Optional[str] = None
    completada: bool = False

class TareaCreate(TareaBase):
    pass

class TareaDB(TareaBase):
    id: int
    creada_en: datetime

    class Config:
        orm_mode = True
