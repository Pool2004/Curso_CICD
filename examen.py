from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API CRUD de Estudiantes")

class Estudiante(BaseModel):
    nombre: str
    nota: float

estudiantes: List[Estudiante] = []

@app.post("/estudiantes", response_model=Estudiante)
def agregar_estudiante(estudiante: Estudiante):
    estudiantes.append(estudiante)
    return estudiante

@app.get("/estudiantes", response_model=List[Estudiante])
def obtener_estudiantes():
    return estudiantes

@app.get("/estudiantes_notas")
def obtener_estudiantes_notas():
    return [{"nombre": e.nombre, "nota": e.nota} for e in estudiantes]

@app.get("/promedio")
def calcular_promedio():
    if not estudiantes:
        return {"promedio": 0}
    promedio = sum(e.nota for e in estudiantes) / len(estudiantes)
    return {"promedio": round(promedio, 2)}

@app.put("/estudiantes/{nombre}", response_model=Estudiante)
def actualizar_estudiante(nombre: str, datos: Estudiante):
    for idx, e in enumerate(estudiantes):
        if e.nombre == nombre:
            estudiantes[idx] = datos
            return datos
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")

@app.delete("/estudiantes/{nombre}")
def eliminar_estudiante(nombre: str):
    for e in estudiantes:
        if e.nombre == nombre:
            estudiantes.remove(e)
            return {"mensaje": f"Estudiante {nombre} eliminado"}
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")
