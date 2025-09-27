# Importa FastAPI para crear la API y HTTPException para manejar errores HTTP
from fastapi import FastAPI, HTTPException
# Importa BaseModel de Pydantic para definir el modelo de datos
from pydantic import BaseModel
# Importa List para definir tipos de listas
from typing import List

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

# Define el modelo de datos Persona con id, nombre y edad
class Persona(BaseModel):
    id: int
    nombre: str
    edad: int

# Base de datos simulada en memoria (lista de personas)
personas_db = []

# Endpoint para crear una nueva persona (POST)
@app.post("/personas/", response_model=Persona)
def crear_persona(persona: Persona):
    personas_db.append(persona)  # Agrega la persona a la base de datos
    return persona  # Retorna la persona creada

# Endpoint para listar todas las personas (GET)
@app.get("/personas/", response_model=List[Persona])
def listar_personas():
    return personas_db  # Retorna la lista de personas

# Endpoint para obtener una persona por su ID (GET)
@app.get("/personas/{persona_id}", response_model=Persona)
def obtener_persona(persona_id: int):
    for persona in personas_db:
        if persona.id == persona_id:  # Busca la persona por ID
            return persona  # Retorna la persona encontrada
    raise HTTPException(status_code=404, detail="Persona no encontrada")  # Si no existe, lanza error 404

# Endpoint para actualizar una persona por su ID (PUT)
@app.put("/personas/{persona_id}", response_model=Persona)
def actualizar_persona(persona_id: int, datos: Persona):
    for idx, persona in enumerate(personas_db):
        if persona.id == persona_id:  # Busca la persona por ID
            personas_db[idx] = datos  # Actualiza los datos de la persona
            return datos  # Retorna la persona actualizada
    raise HTTPException(status_code=404, detail="Persona no encontrada")  # Si no existe, lanza error 404

# Endpoint para eliminar una persona por su ID (DELETE)
@app.delete("/personas/{persona_id}")
def eliminar_persona(persona_id: int):
    for idx, persona in enumerate(personas_db):
        if persona.id == persona_id:  # Busca la persona por ID
            del personas_db[idx]  # Elimina la persona de la base de datos
            return {"detail": "Persona eliminada"}  # Retorna mensaje de éxito
    raise HTTPException(status_code=404, detail="Persona no encontrada")  # Si no existe, lanza error 404

# Pasos para probar la API en Postman:

# 1. **Inicia el servidor FastAPI**
#    - Abre una terminal en la carpeta del archivo.
#    - Ejecuta: `uvicorn api.api:app --reload`
#    - El servidor estará en: `http://127.0.0.1:8000`

# 2. **Abre Postman**

# 3. **Prueba los endpoints:**

#    - **Crear persona (POST)**
#      - Método: POST
#      - URL: `http://127.0.0.1:8000/personas/`
#      - Body (JSON, selecciona "raw" y "JSON"):
#        ```json
#        {  
#          "id": 1,
#          "nombre": "Juan",
#          "edad": 30
#        }
#        ```
#      - Haz clic en "Send".

#    - **Listar personas (GET)**
#      - Método: GET
#      - URL: `http://127.0.0.1:8000/personas/`
#      - Haz clic en "Send".

#    - **Obtener persona por ID (GET)**
#      - Método: GET
#      - URL: `http://127.0.0.1:8000/personas/1`
#      - Haz clic en "Send".

#    - **Actualizar persona (PUT)**
#      - Método: PUT
#      - URL: `http://127.0.0.1:8000/personas/1`
#      - Body (JSON):
#        ```json
#        {
#          "id": 1,
#          "nombre": "Juan Perez",
#          "edad": 31
#        }
#        ```
#      - Haz clic en "Send".

#    - **Eliminar persona (DELETE)**
#      - Método: DELETE
#      - URL: `http://127.0.0.1:8000/personas/1`
#      - Haz clic en "Send".

# 4. **Verifica las respuestas en Postman.**

# Solución al error "uvicorn: command not found":

# 1. Abre una terminal en tu proyecto.
# 2. Instala FastAPI y Uvicorn:
#    ```
#    pip install fastapi uvicorn
#    ```
# 3. Ejecuta el servidor nuevamente:
#    ```
#    uvicorn api.api:app --reload
#    ```