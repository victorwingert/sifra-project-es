from fastapi.testclient import TestClient
from src.models.turma import Turma

def test_list_turmas(client: TestClient, test_turma: Turma):
    response = client.get("/api/v1/turmas/")
    assert response.status_code == 200
    turmas = response.json()
    assert isinstance(turmas, list)
    assert len(turmas) >= 1
    assert any(t["turma_id"] == test_turma.turma_id for t in turmas)

def test_get_turma_discentes_empty(client: TestClient, test_turma: Turma):
    response = client.get(f"/api/v1/turmas/{test_turma.turma_id}/discentes")
    assert response.status_code == 200
    discentes = response.json()
    assert isinstance(discentes, list)
    assert len(discentes) == 0
