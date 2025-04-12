from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient
from hypothesis import HealthCheck, Verbosity, given, settings
from hypothesis import strategies as st
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from api import TodoIn, TodoOut, app, get_session, reg


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    reg.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
        
    reg.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    return client


# Example testing
def test_create_todo(client: TestClient):
    data = {'name': 'sleep', 'description': 'every day'}
    response = client.post('/create', json=data)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == data | {'id': 1}


@given(st.builds(TodoIn))
@settings(
    verbosity=Verbosity.verbose,
    max_examples=100,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
)
def test_create_todo_hypo(client: TestClient, todo):
    response = client.post('/create', json=todo.model_dump())

    assert response.status_code == HTTPStatus.CREATED

    assert TodoOut(**response.json())
