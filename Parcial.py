# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API CRUD con FastAPI - CI/CD")

# ---- Modelo de datos ----
class Item(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None
    precio: float
    disponible: bool = True

# ---- "Base de datos" en memoria ----
db: List[Item] = []

# ---- Métodos CRUD ----

# CREATE
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    # Validamos si el ID ya existe
    for existente in db:
        if existente.id == item.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    db.append(item)
    return item

# READ - todos
@app.get("/items/", response_model=List[Item])
def get_items():
    return db

# READ - por id
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")

# UPDATE
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(db):
        if item.id == item_id:
            db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item no encontrado")

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(db):
        if item.id == item_id:
            db.pop(index)
            return {"mensaje": f"Item con ID {item_id} eliminado"}
    raise HTTPException(status_code=404, detail="Item no encontrado")
