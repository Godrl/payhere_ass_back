from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

from app.main import app
from app.api import deps


# test database connect
db_url = f'mysql+pymysql://root:0902' \
         f'@127.0.0.1/payhere_ass'

engine = create_engine(
    db_url,
    echo=True,  # query logging
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as client:
        app.dependency_overrides[deps.get_db] = override_get_db
        yield client
        app.dependency_overrides = {}


@pytest.fixture(scope='function')
def auth_user(client):
    client.post(f'{settings.API_V1_STR}/auth/login', {'username': 'test@test.com', 'password': '123'})
    # header cookie 에 access_token 저장이 됨
    return None
