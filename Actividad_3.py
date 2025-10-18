#solucion de la actividad 3

#Christian Daniel Bolaños Diaz

#para los detalles de el endpoint -- requeriments.txt 


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API de Créditos Emmanuel")

# Modelo para recibir datos
class Cliente(BaseModel):
    nombre: str
    telefono: str
    direccion: str

# Simulamos una base de datos temporal
clientes_db = []

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de Créditos Emmanuel"}

@app.get("/clientes")
def listar_clientes():
    return {"clientes": clientes_db}

@app.post("/clientes")
def crear_cliente(cliente: Cliente):
    clientes_db.append(cliente.dict())
    return {"mensaje": "Cliente creado exitosamente", "cliente": cliente}
