import importlib

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from ...utils import needs_py39


@pytest.fixture(
    name="app",
    params=[
        "tutorial003",
        pytest.param("tutorial003_py39", marks=needs_py39),
    ],
)
def get_app(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"docs_src.websockets.{request.param}")
    return mod.app


@pytest.fixture(
    name="html",
    params=[
        "tutorial003",
        pytest.param("tutorial003_py39", marks=needs_py39),
    ],
)
def get_html(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"docs_src.websockets.{request.param}")
    return mod.html


@pytest.fixture(name="client")
def get_client(app: FastAPI):
    client = TestClient(app)
    return client


def test_get(client: TestClient, html: str):
    response = client.get("/")
    assert response.text == html


def test_websocket_handle_disconnection(client: TestClient):
    with client.websocket_connect("/ws/1234") as connection, client.websocket_connect(
        "/ws/5678"
    ) as connection_two:
        connection.send_text("Hello from 1234")
        data1 = connection.receive_text()
        assert data1 == "You wrote: Hello from 1234"
        data2 = connection_two.receive_text()
        client1_says = "Client #1234 says: Hello from 1234"
        assert data2 == client1_says
        data1 = connection.receive_text()
        assert data1 == client1_says
        connection_two.close()
        data1 = connection.receive_text()
        assert data1 == "Client #5678 left the chat"
