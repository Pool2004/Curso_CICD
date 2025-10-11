import pytest 
# Importamos el cliente de prueba de FastAPI
from fastapi.testclient import TestClient 
import sys
import os

# --- INICIO: MANEJO DE RUTA PARA IMPORTACIÓN ---

# Obtiene la ruta de la carpeta 'test'
current_dir = os.path.dirname(os.path.abspath(__file__))
# Sube UN NIVEL para obtener la ruta de 'actividad_3'
parent_dir = os.path.dirname(current_dir)

# Añadir 'actividad_3' al path
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Importa el objeto 'app' desde el archivo 'parcial_api.py'
from parcial_api import app 

# --- FIN: MANEJO DE RUTA PARA IMPORTACIÓN ---

# 1. Crea la instancia del TestClient UNA SOLA VEZ fuera de las funciones de prueba
# Esta es la clase correcta que acepta el argumento 'app'
client = TestClient(app) 

# 2. La función de prueba ahora es SÍNCRONA
def test_crear_tarea():
    # Usamos el cliente creado
    response = client.post("/tareas/", json={
        "id": 1,
        "nombre": "Tarea 1",
        "descripcion": "Descripción de la tarea 1",
        "completada": False
    })
    
    # Verificaciones
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nombre": "Tarea 1",
        "descripcion": "Descripción de la tarea 1",
        "completada": False
    }