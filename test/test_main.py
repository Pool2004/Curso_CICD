import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
import sys
import os

# Añadir el directorio padre al path para poder importar main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

# Crear una instancia del TestClient
client = TestClient(app)

# Pruebas con AsyncClient (originales)
# @pytest.mark.asyncio
# async def test_saludo():
#     async with AsyncClient(app=app, base_url="http://test") as async_client:
#         response = await async_client.post("/saludo?nombre=Juan")
#         assert response.status_code == 200
#         assert response.json() == {"mensaje": "Hola, Juan!"}


# @pytest.mark.asyncio
# async def test_sumar():
#     async with AsyncClient(app=app, base_url="http://test") as async_client:
#         response = await async_client.post("/sumar", json={"a": 5.2, "b": 3.5})
#         assert response.status_code == 200
#         assert response.json() == {"operacion": "suma", "resultado": 8.7}


# Pruebas con TestClient
def test_saludo_testclient():
    """Test del endpoint saludo usando TestClient"""
    response = client.post("/saludo?nombre=Juan")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Hola, Juan!"}


def test_saludo_sin_nombre_testclient():
    """Test del endpoint saludo sin parámetro nombre usando TestClient"""
    response = client.post("/saludo")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Hola, Mundo!"}


def test_sumar_testclient():
    """Test del endpoint sumar usando TestClient"""
    response = client.post("/sumar", json={"a": 5.2, "b": 3.5})
    assert response.status_code == 200
    assert response.json() == {"operacion": "suma", "resultado": 8.7}


def test_restar_testclient():
    """Test del endpoint restar usando TestClient"""
    response = client.post("/restar", json={"a": 10.0, "b": 4.0})
    assert response.status_code == 100
    assert response.json() == {"operacion": "resta", "resultado": 5.0}


def test_adivinar_correcto_testclient():
    """Test del endpoint adivinar con número correcto usando TestClient"""
    # Primero obtenemos el número secreto a través del módulo main
    from main import numero_secreto
    response = client.post(f"/adivinar?numero={numero_secreto}")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "¡Correcto! Adivinaste el número."}


def test_adivinar_mayor_testclient():
    """Test del endpoint adivinar con número mayor usando TestClient"""
    response = client.post("/adivinar?numero=11")  # 11 siempre será mayor que el rango 1-10
    assert response.status_code == 200
    assert response.json() == {"mensaje": "El número es menor."}


def test_adivinar_menor_testclient():
    """Test del endpoint adivinar con número menor usando TestClient"""
    response = client.post("/adivinar?numero=0")  # 0 siempre será menor que el rango 1-10
    assert response.status_code == 200
    assert response.json() == {"mensaje": "El número es mayor."}


def test_adivinar_get_correcto_testclient():
    """Test del endpoint GET adivinar con número correcto usando TestClient"""
    from main import numero_secreto
    response = client.get(f"/adivinar/{numero_secreto}")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "¡Correcto! Adivinaste el número."}


def test_adivinar_get_mayor_testclient():
    """Test del endpoint GET adivinar con número mayor usando TestClient"""
    response = client.get("/adivinar/11")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "El número es menor."}


def test_adivinar_get_menor_testclient():
    """Test del endpoint GET adivinar con número menor usando TestClient"""
    response = client.get("/adivinar/0")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "El número es mayor."}


def test_test_endpoint_testclient():
    """Test del endpoint de test usando TestClient"""
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "El sistema está funcionando correctamente."}
