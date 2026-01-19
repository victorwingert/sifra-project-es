from fastapi.testclient import TestClient
from sqlmodel import Session

from src.models.usuario import Usuario

def get_auth_headers(client: TestClient, email: str, password: str) -> dict[str, str]:
    """Função auxiliar para autenticar e retornar os headers de autorização."""
    login_data = {"username": email, "password": password}
    response = client.post("/api/v1/auth/token", data=login_data)
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_read_user_me(client: TestClient, test_user: Usuario):
    headers = get_auth_headers(client, test_user.email, "senha123")
    response = client.get("/api/v1/usuario/me", headers=headers)
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["email"] == test_user.email


def test_get_usuarios(client: TestClient, test_user: Usuario):
    response = client.get("/api/v1/usuario/")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert any(user["email"] == test_user.email for user in users)


def test_get_usuario_by_id(client: TestClient, test_user: Usuario):
    response = client.get(f"/api/v1/usuario/{test_user.usuario_id}")
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["usuario_id"] == test_user.usuario_id
