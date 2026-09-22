from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_root_conteudo():
    response = client.get("/")
    assert response.json() == {"message": "Hello, World!"}


def test_teste1_status_code():
    response = client.get("/teste1")
    assert response.status_code == 200


def test_teste1_valor_booleano():
    response = client.get("/teste1")
    data = response.json()

    assert data["teste"] is True


def test_teste1_numero_aleatorio():
    response = client.get("/teste1")
    data = response.json()

    assert isinstance(data["num_aleatorio"], int)
    assert 0 <= data["num_aleatorio"] <= 1000