
"""Application FastAPI pour les opérations mathématiques et la gestion d'éléments."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Retourne un message de bienvenue."""
    return {"message": "it works !"}


@app.get("/addition")
def add_numbers(a: int, b: int):
    """Additionne deux nombres entiers."""
    return {"result a+b=": a + b, "developer": "Dev1"}


@app.post("/multiply")
def multiply_numbers(a: int, b: int):
    """Multiplie deux nombres entiers."""
    return {"result a*b=": a * b, "developer": "Dev2"}


@app.post("/divide")
def divide_numbers(a: int, b: int):
    """Divise deux nombres et gère la division par zéro."""
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result a/b=": a / b, "developer": "Leader"}


@app.delete("/remove/{item_id}")
def delete_item(item_id: int):
    """Supprime un élément à partir de son identifiant."""
    return {"message": f"Item {item_id} deleted successfully"}


@app.put("/update/{item_id}")
def update_item(item_id: int, name: str):
    """Met à jour le nom d'un élément."""
    return {
        "message": f"Item {item_id} updated successfully",
        "new_name": name
    }


@app.get("/subtraction")
def subtract_numbers(a: int, b: int):
    """Soustrait le deuxième nombre du premier."""
    return {"result a-b=": a - b, "developer": "Dev3"}
