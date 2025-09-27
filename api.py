from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Frase(BaseModel):
    id: int
    texto: str

frases = [
    Frase(id=1, texto="El éxito es la suma de pequeños esfuerzos repetidos cada día."),
    Frase(id=2, texto="La disciplina tarde o temprano vencerá a la inteligencia."),
    Frase(id=3, texto="No cuentes los días, haz que los días cuenten."),
]

@app.get("/frases")
def get_frases():
    return frases

@app.get("/frases/{frase_id}")
def get_frase(frase_id: int):
    for frase in frases:
        if frase.id == frase_id:
            return frase
    return {"error": "Frase no encontrada"}

@app.post("/frases")
def add_frase(frase: Frase):
    frases.append(frase)
    return {"mensaje": "Frase agregada", "frase": frase}

@app.put("/frases/{frase_id}")
def update_frase(frase_id: int, frase_actualizada: Frase):
    for i, frase in enumerate(frases):
        if frase.id == frase_id:
            frases[i] = frase_actualizada
            return {"mensaje": "Frase actualizada", "frase": frase_actualizada}
    return {"error": "Frase no encontrada"}

@app.delete("/frases/{frase_id}")
def delete_frase(frase_id: int):
    for i, frase in enumerate(frases):
        if frase.id == frase_id:
            frases.pop(i)
            return {"mensaje": "Frase eliminada"}
    return {"error": "Frase no encontrada"}