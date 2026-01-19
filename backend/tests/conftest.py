import pytest
import uuid
from fastapi.testclient import TestClient
from sqlmodel import Session, create_engine, select

from src.main import app
from src.db.session import get_session
from src.core.config import settings
from src.models.usuario import Usuario
from src.models.disciplina import Disciplina
from src.models.docente import Docente
from src.models.turma import Turma

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

@pytest.fixture(name="test_user")
def test_user_fixture(session: Session):
    uid = str(uuid.uuid4())[:8]
    user = Usuario(
        nome=f"User {uid}",
        email=f"user_{uid}@test.com",
        senha="senha123",
        tipo_usuario="discente"
    )
    session.add(user)
    session.flush()
    session.refresh(user)
    return user

@pytest.fixture(name="test_admin")
def test_admin_fixture(session: Session):
    uid = str(uuid.uuid4())[:8]
    admin = Usuario(
        nome=f"Admin {uid}",
        email=f"admin_{uid}@test.com",
        senha="adminpassword",
        tipo_usuario="ADMIN"
    )
    session.add(admin)
    session.flush()
    session.refresh(admin)
    return admin

@pytest.fixture(name="test_disciplina")
def test_disciplina_fixture(session: Session):
    uid = str(uuid.uuid4())[:8]
    disciplina = Disciplina(
        codigo=f"D_{uid}",
        nome=f"Disciplina {uid}",
        carga_horaria=60,
        faltas_permitidas=15
    )
    session.add(disciplina)
    session.flush()
    session.refresh(disciplina)
    return disciplina

@pytest.fixture(name="test_docente")
def test_docente_fixture(session: Session):
    uid = str(uuid.uuid4())[:8]
    user = Usuario(
        nome=f"Docente {uid}",
        email=f"docente_{uid}@test.com",
        senha="docentepassword",
        tipo_usuario="DOCENTE"
    )
    session.add(user)
    session.flush()
    session.refresh(user)
    
    docente = Docente(usuario_id=user.usuario_id, departamento="Computação")
    session.add(docente)
    session.flush()
    session.refresh(docente)
    return docente

@pytest.fixture(name="test_turma")
def test_turma_fixture(session: Session, test_disciplina: Disciplina, test_docente: Docente):
    turma = Turma(
        ano=2024,
        semestre="1",
        disciplina_id=test_disciplina.disciplina_id,
        docente_id=test_docente.usuario_id
    )
    session.add(turma)
    session.flush()
    session.refresh(turma)
    return turma
