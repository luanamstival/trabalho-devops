from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_teste1():
    response = client.get("/teste1")

    assert response.status_code == 200

    data = response.json()

    assert data["teste"] is True
    assert 0 <= data["num_aleatorio"] <= 1000
