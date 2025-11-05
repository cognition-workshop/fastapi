import importlib
from base64 import b64encode

import pytest
from fastapi.testclient import TestClient

from ...utils import needs_py39


@pytest.fixture(
    name="client",
    params=[
        "tutorial007",
        "tutorial007_an",
        pytest.param("tutorial007_an_py39", marks=needs_py39),
    ],
)
def get_client(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"docs_src.security.{request.param}")

    client = TestClient(mod.app)
    return client


def test_security_http_basic_correct_credentials(client: TestClient):
    response = client.get("/users/me", auth=("stanleyjobson", "swordfish"))
    assert response.status_code == 200, response.text
    assert response.json() == {"username": "stanleyjobson"}


def test_security_http_basic_incorrect_username(client: TestClient):
    response = client.get("/users/me", auth=("wrong", "swordfish"))
    assert response.status_code == 401, response.text
    assert response.json() == {"detail": "Incorrect username or password"}
    assert response.headers["WWW-Authenticate"] == "Basic"


def test_security_http_basic_incorrect_password(client: TestClient):
    response = client.get("/users/me", auth=("stanleyjobson", "wrong"))
    assert response.status_code == 401, response.text
    assert response.json() == {"detail": "Incorrect username or password"}
    assert response.headers["WWW-Authenticate"] == "Basic"


def test_security_http_basic_no_credentials(client: TestClient):
    response = client.get("/users/me")
    assert response.status_code == 401, response.text
    assert response.json() == {"detail": "Not authenticated"}
    assert response.headers["WWW-Authenticate"] == "Basic"


def test_security_http_basic_invalid_credentials(client: TestClient):
    response = client.get(
        "/users/me", headers={"Authorization": "Basic notabase64token"}
    )
    assert response.status_code == 401, response.text
    assert response.headers["WWW-Authenticate"] == "Basic"
    assert response.json() == {"detail": "Invalid authentication credentials"}


def test_security_http_basic_non_basic_credentials(client: TestClient):
    payload = b64encode(b"stanleyjobsonswordfish").decode("ascii")
    auth_header = f"Basic {payload}"
    response = client.get("/users/me", headers={"Authorization": auth_header})
    assert response.status_code == 401, response.text
    assert response.headers["WWW-Authenticate"] == "Basic"
    assert response.json() == {"detail": "Invalid authentication credentials"}


def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "FastAPI", "version": "0.1.0"},
        "paths": {
            "/users/me": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "summary": "Read Current User",
                    "operationId": "read_current_user_users_me_get",
                    "security": [{"HTTPBasic": []}],
                }
            }
        },
        "components": {
            "securitySchemes": {"HTTPBasic": {"type": "http", "scheme": "basic"}}
        },
    }
