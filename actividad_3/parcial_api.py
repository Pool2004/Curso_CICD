from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI()


class Tareas(BaseModel):
    id: int
    nombre: str
    descripcion: str
    completada: bool


tareas_db: List[Tareas] = []


@app.post("/tareas/", response_model=Tareas)
def crear_tarea(tarea: Tareas):
    tareas_db.append(tarea)
    return tarea

@app.get("/tareas/", response_model=List[Tareas])
def obtener_tareas():
    return tareas_db


@app.get("/tareas/{tarea_id}", response_model=Tareas)
def obtener_tarea(tarea_id: int):
    for tarea in tareas_db:
        if tarea.id == tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")



@app.put("/tareas/{tarea_id}", response_model=Tareas)
def actualizar_tarea(tarea_id: int, tarea_actualizada: Tareas):
    for index, tarea in enumerate(tareas_db):
        if tarea.id == tarea_id:
            tareas_db[index] = tarea_actualizada
            return tarea_actualizada
    raise HTTPException(status_code=404, detail="Tarea no encontrada")      



@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int):
    for index, tarea in enumerate(tareas_db):
        if tarea.id == tarea_id:
            del tareas_db[index]
            return {"detail": "Tarea eliminada"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")



@app.patch("/tareas/{tarea_id}/completar", response_model=Tareas)
def completar_tarea(tarea_id: int):
    for tarea in tareas_db:
        if tarea.id == tarea_id:
            tarea.completada = True
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")