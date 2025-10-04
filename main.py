from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Modelo para operaciones matemáticas
class Operacion(BaseModel):
    a: float
    b: float

# Variable global para el número secreto
numero_secreto = random.randint(1, 10)

@app.get("/saludo")
def saludo(nombre: str = "Mundo"):
    return {"mensaje": f"Hola, {nombre}!"}

@app.post("/sumar")
def sumar(datos: Operacion):
    resultado = datos.a + datos.b
    return {"operacion": "suma", "resultado": resultado}

@app.post("/restar")
def restar(datos: Operacion):
    resultado = datos.a - datos.b
    return {"operacion": "resta", "resultado": resultado}

@app.get("/adivinar")
def adivinar(numero: int):
    if numero == numero_secreto:
        return {"mensaje": "¡Correcto! Adivinaste el número."}
    elif numero < numero_secreto:
        return {"mensaje": "El número es mayor."}
    else:
        return {"mensaje": "El número es menor."}