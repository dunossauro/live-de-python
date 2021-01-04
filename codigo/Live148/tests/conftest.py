import pytest
from sqlalchemy.engine import create_engine
from sqlalchemy_utils import drop_database
from starlette.config import environ
from starlette.testclient import TestClient

environ["TESTING"] = "True"

from app.database import TEST_DATABASE_URL, metadata
from app.models import User
from run import app


@pytest.mark.asyncio
@pytest.fixture(autouse=True)
async def create_user_db():
    url = str(TEST_DATABASE_URL)

    engine = create_engine(url)
    metadata.create_all(engine)

    await User.objects.create(
        name="Dunossauro",
        email="du@email.com",
        password="1234"
    )

    yield
    drop_database(url)


@pytest.fixture()
def client():
    with TestClient(app) as Client:
        return Client
