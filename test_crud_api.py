import requests
import pytest

#Api gratuita para pruebas
BASE_URL = "https://jsonplaceholder.typicode.com"

# --- 1. POST: Crear un nuevo recurso ---
def test_create_post():
    # Datos que se mandan al servidor
    payload = {
        "title": "Mi primer proyecto QA",
        "body": "Automatizando pruebas con PyTest",
        "userId": 1
    }
    
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    # Verificar el código 201 en HTTP
    assert response.status_code == 201, f"Error: Código {response.status_code}"
    
    # Validamos que el servidor nos devuelva los datos que enviamos
    data = response.json()
    assert data["title"] == payload["title"], "El título no coincide"


# --- 2. PUT: Actualizar un recurso existente ---
def test_update_post():
    # Actualizar el Post número 1
    post_id = 1
    payload_actualizado = {
        "id": 1,
        "title": "Título actualizado por QA",
        "body": "Este texto fue modificado",
        "userId": 1
    }
    
    # Usamos requests.put() a la ruta específica del post
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload_actualizado)
    
    # 200 significa "OK" (Se actualizó bien)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Título actualizado por QA"


# --- 3. DELETE: Borrar un recurso ---
def test_delete_post():
    # Prueba para borrar el Post número 1
    post_id = 1
    
    # Usamos requests.delete()
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    
    # 200 (OK) o 204 (No Content) son respuestas válidas para un borrado exitoso
    assert response.status_code in [200, 204], f"Error al borrar, código: {response.status_code}"