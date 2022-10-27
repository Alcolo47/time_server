import pytest
from starlette.testclient import TestClient

from time_server.main import app


@pytest.fixture(scope="module")
def client():
    yield TestClient(app=app)


def test_api_root(client):
    response = client.get('/').json()
    assert 'timestamp' in response
