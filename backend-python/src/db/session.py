from collections.abc import Generator

from sqlmodel import Session, create_engine

from ..core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_size=10,
    max_overflow=20,
)


def get_session() -> Generator[Session]:
    with Session(engine) as session:
        yield session
