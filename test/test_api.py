import sys
import os
# Añadir el directorio padre al path para poder importar main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
import httpx
from api_desplegar.api import app

@pytest.mark.asyncio
async def test_get_frases():
    async with httpx.AsyncClient(base_url="http://test") as ac:
        # Usa el servidor de pruebas de FastAPI
        from fastapi import FastAPI
        from fastapi.testclient import TestClient

        with TestClient(app) as client:
            response = client.get("/frases")
            assert response.status_code == 200
            assert len(response.json()) == 3