import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

# Prueba 1: Verificar que la API responde con éxito (Código HTTP 200)
def test_get_user_success():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200, f"Se esperaba código 200, pero se obtuvo {response.status_code}"

# Prueba 2: Verificar que la estructura JSON contenga los datos correctos
def test_user_data_structure():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    
    assert "name" in data, "Error: Falta el campo 'name'"
    assert "email" in data, "Error: Falta el campo 'email'"

# Prueba 3: Prueba Negativa (Validar respuesta ante un usuario inexistente)
def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/9999")
    
    # Para un usuario que no existe, la API debe devolver un error 404 (Not Found)
    assert response.status_code == 404, f"Se esperaba código 404, pero se obtuvo {response.status_code}"