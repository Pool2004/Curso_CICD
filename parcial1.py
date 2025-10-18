from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

paises=[]

@app.post("/paises")
def resgistrar_pais(pais:dict):
    pais["id"] = len(paises) +1
    paises.append(pais)
    return pais

@app.get("/lista")
def lista_de_paises():
    return paises

@app.get("/pais/{pais_id}")
def traer_pais(pais_id: int):
    for p in paises:
        if p["id"]==pais_id:
            return p
@app.put("/actualizar_pais/{pais_id}")
def actualizar_pais(pais_id:int, datos: dict):
    for p in paises:
        if p["id"]==pais_id:
            p.update(datos)
            p["id"]= pais_id
            return p    

@app.delete("/borrar_pais/{pais_id}")   
def eliminar_pais(pais_id: int):
    for i, p in enumerate(paises):
        if p["id"]==pais_id:
            paises.pop(i)
            return {"mensaje":f"pais {pais_id} ha sido eliminado"}         