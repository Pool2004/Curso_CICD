from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import json
import pathlib
import os

BASE_DIR = pathlib.Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "contacts.json"
TEMPLATES_DIR = BASE_DIR.parent / "templates"
STATIC_DIR = BASE_DIR.parent / "frontend"

app = FastAPI()

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# CORS para desarrollo en Docker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Acepta peticiones de cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

def load_contacts():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


@app.get("/contactos")
def obtener_contactos():
    return load_contacts()

# Página principal
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    contacts = load_contacts()
    return templates.TemplateResponse("index.html", {"request": request, "contacts": contacts})

# Formulario nuevo contacto
@app.get("/new", response_class=HTMLResponse)
async def new_contact_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# Agregar contacto
@app.post("/add")
async def add_contact(name: str = Form(...), phone: str = Form(...)):
    contacts = load_contacts()
    new_id = max([c["id"] for c in contacts], default=0) + 1
    contacts.append({"id": new_id, "name": name, "phone": phone})
    save_contacts(contacts)
    return RedirectResponse("/", status_code=303)
# editar contacto
@app.get("/edit/{contact_id}", response_class=HTMLResponse)
async def edit_contact_form(request: Request, contact_id: int):
    contacts = load_contacts()
    contact = next((c for c in contacts if c["id"] == contact_id), None)
    if contact:
        return templates.TemplateResponse("edit.html", {"request": request, "contact": contact})
    return RedirectResponse("/", status_code=303)

# Actualizar contacto
@app.post("/update/{contact_id}")
async def update_contact(contact_id: int, name: str = Form(...), phone: str = Form(...)):
    contacts = load_contacts()
    for c in contacts:
        if c["id"] == contact_id:
            c["name"] = name
            c["phone"] = phone
            break
    save_contacts(contacts)
    return RedirectResponse("/", status_code=303)

# Eliminar contacto
@app.get("/delete/{contact_id}")
async def delete_contact(contact_id: int):
    contacts = load_contacts()
    contacts = [c for c in contacts if c["id"] != contact_id]
    save_contacts(contacts)
    return RedirectResponse("/", status_code=303)
