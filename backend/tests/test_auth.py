from fastapi.testclient import TestClient
from src.models.usuario import Usuario

def test_login_access_token(client: TestClient, test_user: Usuario):
    login_data = {
        "username": test_user.email,
        "password": "senha123",
    }
    response = client.post("/api/v1/auth/token", data=login_data)
    assert response.status_code == 200
    token = response.json()
    assert "access_token" in token
    assert token["token_type"] == "bearer"
