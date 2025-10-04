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

@app.post("/saludo")
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

@app.post("/adivinar")
def adivinar(numero: int):
    if numero == numero_secreto:
        return {"mensaje": "¡Correcto! Adivinaste el número."}
    elif numero < numero_secreto:
        return {"mensaje": "El número es mayor."}
    else:
        return {"mensaje": "El número es menor."}
    

@app.get("/test")
def test():
    return {"mensaje": "El sistema está funcionando correctamente."}

@app.get("/adivinar/{numero}")
def adivinar_get(numero: int):
    if numero == numero_secreto:
        return {"mensaje": "¡Correcto! Adivinaste el número."} 
    elif numero < numero_secreto:
        return {"mensaje": "El número es mayor."}
    else:
        return {"mensaje": "El número es menor."}
    

# Endpoint para reiniciar el número secreto
@app.post("/reiniciar")
def reiniciar():
    global numero_secreto
    numero_secreto = random.randint(1, 10)
    return {"mensaje": "El número secreto ha sido reiniciado."}

# Endpoint para obtener el número secreto (solo para pruebas)
@app.get("/numero_secreto")
def obtener_numero_secreto():
    return {"numero_secreto": numero_secreto}

