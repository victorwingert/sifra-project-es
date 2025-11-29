from contextlib import contextmanager
from sqlmodel import create_engine, Session
from app.core.config import settings

def _get_engine(database_name: str, **kwargs):
    url = settings.DATABASE_URL + database_name
    return create_engine(url, **kwargs)

@contextmanager
def get_db(database_name: str):
    engine = _get_engine(database_name)
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
