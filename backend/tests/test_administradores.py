from fastapi.testclient import TestClient
from src.models.usuario import Usuario

def get_auth_headers(client: TestClient, email: str, password: str) -> dict[str, str]:
    login_data = {"username": email, "password": password}
    response = client.post("/api/v1/auth/token", data=login_data)
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_create_administrador(client: TestClient, test_admin: Usuario):
    headers = get_auth_headers(client, test_admin.email, "adminpassword")
    
    new_admin_data = {
        "nome": "Novo Admin",
        "email": "novoadmin@exemplo.com",
        "senha": "newpassword123",
        "telefone": "123456789"
    }
    
    response = client.post(
        "/api/v1/administradores/",
        json=new_admin_data,
        headers=headers
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "novoadmin@exemplo.com"
    assert data["nome"] == "Novo Admin"
    assert data["tipo_usuario"] == "ADMIN"
