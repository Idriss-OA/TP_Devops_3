
"""Tests unitaires des endpoints de l'application FastAPI."""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    """Teste la réponse de la page d'accueil."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "it works !"}


def test_addition():
    """Teste l'addition de deux nombres."""
    response = client.get("/addition?a=10&b=5")
    assert response.status_code == 200
    assert response.json()["result a+b="] == 15


def test_multiply():
    """Teste la multiplication de deux nombres."""
    response = client.post("/multiply?a=10&b=5")
    assert response.status_code == 200
    assert response.json()["result a*b="] == 50


def test_divide():
    """Teste la division de deux nombres."""
    response = client.post("/divide?a=10&b=5")
    assert response.status_code == 200
    assert response.json()["result a/b="] == 2


def test_divide_by_zero():
    """Teste la gestion de la division par zéro."""
    response = client.post("/divide?a=10&b=0")
    assert response.status_code == 200
    assert response.json() == {
        "error": "Division by zero is not allowed"
    }


def test_delete_item():
    """Teste la suppression d'un élément."""
    response = client.delete("/remove/1")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item 1 deleted successfully"
    }


def test_update_item():
    """Teste la modification d'un élément."""
    response = client.put("/update/1?name=NewName")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item 1 updated successfully",
        "new_name": "NewName"
    }


def test_subtraction():
    """Teste une soustraction positive."""
    response = client.get("/subtraction?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {
        "result a-b=": 5,
        "developer": "Dev3"
    }


def test_subtraction_negative():
    """Teste une soustraction avec un résultat négatif."""
    response = client.get("/subtraction?a=5&b=10")
    assert response.status_code == 200
    assert response.json()["result a-b="] == -5


def test_subtraction_zero():
    """Teste une soustraction dont le résultat est nul."""
    response = client.get("/subtraction?a=8&b=8")
    assert response.status_code == 200
    assert response.json()["result a-b="] == 0
