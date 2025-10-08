import pytest
from httpx import AsyncClient
import sys
import os

# Añadir el directorio padre al path para poder importar main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

@pytest.mark.asyncio
async def test_saludo():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/saludo?nombre=Juan")
        assert response.status_code == 200
        assert response.json() == {"mensaje": "Hola, Juan!"}


@pytest.mark.asyncio
async def test_sumar():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/sumar", json={"a": 5.2, "b": 3.5})
        assert response.status_code == 200
        assert response.json() == {"operacion": "suma", "resultado": 8.7}
