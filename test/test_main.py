from fastapi.testclient import TestClient

# Pruebas asincrónicas con pytest-asyncio

import pytest
# from httpx import AsyncClient


# Salir de la carpeta actual para importar app desde main.py
import sys
import os
# Agregar el directorio padre al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)



"""
Pruebas para los endpoints de la aplicación FastAPI.

def test_saludo() -> Status code y Json esperado.


"""

# - - - - - - - - - - - - - - - - -- -  - - -- - 

"""
Tests para el endpoint /saludo.

Testing by: Jean

Caso de prueba: Verificar que el endpoint /saludo devuelve el mensaje correcto cuando se proporciona un nombre.

Resultado esperado: El endpoint debe devolver un código de estado 200 y un mensaje de saludo personalizado.
"""
def test_saludo():
    response = client.post("/saludo?nombre=Jean")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Hola, Jean!"}

"""
Test para el endpoint /sumar.

Testing by: Jean

Caso de prueba: Verificar que el endpoint /sumar devuelve la suma correcta de dos números.

Resultado esperado: El endpoint debe devolver un código de estado 200 y el resultado de la suma (8.7) en formato JSON.
"""

def test_sumar():
    response = client.post("/sumar", json={"a": 5.2, "b": 3.5})
    assert response.status_code == 200
    assert response.json() == {"operacion": "suma", "resultado": 8.7}


"""
Test para el endpoint /saludo.

Testing by: Jean

Caso de prueba: Verificar que el endpoint /saludo devuelve el mensaje correcto cuando se proporciona un nombre.

Resultado esperado: El endpoint debe devolver un código de estado 200 y un mensaje de saludo personalizado.
"""
# @pytest.mark.asyncio
# async def test_saludo():
#     from httpx import ASGITransport
#     async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as async_client:
#         response = await async_client.post("/saludo?nombre=Juan")
#         assert response.status_code == 200
#         assert response.json() == {"mensaje": "Hola, Juan!"}

# """
# Test para el endpoint /sumar.
# Testing by: Jean
# Caso de prueba: Verificar que el endpoint /sumar devuelve la suma correcta de dos números.
# Resultado esperado: El endpoint debe devolver un código de estado 200 y el resultado de la suma (8.7) en formato JSON.

# """
# @pytest.mark.asyncio
# async def test_sumar():
#     from httpx import ASGITransport
#     async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as async_client:
#         response = await async_client.post("/sumar", json={"a": 5.2, "b": 3.5})
#         assert response.status_code == 200
#         assert response.json() == {"operacion": "suma", "resultado": 8.7}

