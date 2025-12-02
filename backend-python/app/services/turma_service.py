from app.db.session import get_db
from app.models.turma import Turma
from sqlmodel import select

def get_turmas():
    with get_db("teste") as session:
        statement = (select(Turma))

        result = session.exec(statement).all()

        return result
