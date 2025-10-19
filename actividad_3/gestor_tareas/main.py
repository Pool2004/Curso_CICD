from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from database import SessionLocal, init_db, Tarea
from models import TareaCreate, TareaDB

app = FastAPI(title="Gestor de Tareas (PostgreSQL)", version="2.0")

# Inicializar base de datos
init_db()

# Dependencia para obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- RUTAS DE LA API ---
@app.get("/api/tareas", response_model=list[TareaDB])
def obtener_tareas(db: Session = Depends(get_db)):
    return db.query(Tarea).all()

@app.post("/api/tareas", response_model=TareaDB)
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    nueva = Tarea(**tarea.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@app.put("/api/tareas/{tarea_id}", response_model=TareaDB)
def actualizar_tarea(tarea_id: int, tarea: TareaCreate, db: Session = Depends(get_db)):
    existente = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not existente:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    for campo, valor in tarea.dict().items():
        setattr(existente, campo, valor)
    db.commit()
    db.refresh(existente)
    return existente

@app.delete("/api/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    existente = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not existente:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(existente)
    db.commit()
    return {"mensaje": "Tarea eliminada"}

# --- FRONTEND ---
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def raiz():
    return FileResponse("static/index.html")
