import os
import json
import shutil
import tempfile

import pytest
from fastapi.testclient import TestClient

# Importar la aplicación desde el proyecto
from backend.main import app, DATA_FILE


@pytest.fixture(autouse=True)
def isolate_contacts_file(tmp_path, monkeypatch):
    """Use a temporary contacts.json for each test and restore afterwards."""
    # crear una ruta de archivo temporal
    temp_file = tmp_path / "contacts.json"
    temp_file.write_text("[]")

    # monkeypatch el nombre DATA_FILE usado en main.py
    monkeypatch.setattr("main.DATA_FILE", str(temp_file))

    yield

    # La limpieza es automática con tmp_path


@pytest.fixture
def client():
    return TestClient(app)


def test_index_empty(client):
    r = client.get("/")
    assert r.status_code == 200
    # Verificar que la página contiene el texto esperado
    assert "Lista de contactos" in r.text or "lista de contactos" in r.text.lower()

# Crear nuevo contacto
def test_new_contact_form(client):
    r = client.get("/new")
    assert r.status_code == 200
    assert "name" in r.text.lower()

# Agregar y listar contacto
def test_add_and_list_contact(client):
    # add contact
    r = client.post("/add", data={"name": "Alice", "phone": "123"})
    # POST redirects to /
    assert r.status_code in (303, 307, 200)

    # now index should include the contact
    r = client.get("/")
    assert r.status_code == 200
    assert "Alice" in r.text
    assert "123" in r.text

# Editar y actualizar contacto
def test_edit_and_update_contact(client):
    # agregar un contacto
    client.post("/add", data={"name": "Bob", "phone": "555"})

    # editar formulario
    r = client.get("/edit/1")
    assert r.status_code == 200
    assert "Bob" in r.text

    # actualizar contacto
    r = client.post("/update/1", data={"name": "Bobby", "phone": "777"})
    assert r.status_code in (303, 307, 200)

    r = client.get("/")
    assert "Bobby" in r.text
    assert "777" in r.text

# Eliminar contacto
def test_delete_contact(client):
    client.post("/add", data={"name": "Eve", "phone": "999"})
    r = client.get("/delete/1")
    assert r.status_code in (303, 307, 200)
    r = client.get("/")
    assert "Eve" not in r.text
