from fastapi.testclient import TestClient
from API.main import app, personas_db

client = TestClient(app)

def clear_db():
    personas_db.clear()

def test_crear_persona():
    clear_db()
    payload = {"id": 1, "nombre": "Alice", "edad": 30}
    resp = client.post("/personas/", json=payload)
    assert resp.status_code == 200
    assert resp.json() == payload

def test_listar_personas():
    clear_db()
    p1 = {"id": 1, "nombre": "Alice", "edad": 30}
    p2 = {"id": 2, "nombre": "Bob", "edad": 25}
    client.post("/personas/", json=p1)
    client.post("/personas/", json=p2)
    resp = client.get("/personas/")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert p1 in data and p2 in data

def test_obtener_persona():
    clear_db()
    p = {"id": 1, "nombre": "Alice", "edad": 30}
    client.post("/personas/", json=p)
    resp = client.get("/personas/1")
    assert resp.status_code == 200
    assert resp.json() == p

def test_actualizar_persona():
    clear_db()
    original = {"id": 1, "nombre": "Alice", "edad": 30}
    updated = {"id": 1, "nombre": "Alicia", "edad": 31}
    client.post("/personas/", json=original)
    resp = client.put("/personas/1", json=updated)
    assert resp.status_code == 200
    assert resp.json() == updated
    # confirm persisted
    resp2 = client.get("/personas/1")
    assert resp2.status_code == 200
    assert resp2.json() == updated

def test_eliminar_persona():
    clear_db()
    p = {"id": 1, "nombre": "Alice", "edad": 30}
    client.post("/personas/", json=p)
    resp = client.delete("/personas/1")
    assert resp.status_code == 200
    assert resp.json() == {"detail": "Persona eliminada"}
    # confirm not found afterwards
    resp2 = client.get("/personas/1")
    assert resp2.status_code == 404

def test_endpoints_return_404_for_missing():
    clear_db()
    resp_get = client.get("/personas/999")
    assert resp_get.status_code == 404
    resp_put = client.put("/personas/999", json={"id":999,"nombre":"X","edad":0})
    assert resp_put.status_code == 404
    resp_del = client.delete("/personas/999")
    assert resp_del.status_code == 404
