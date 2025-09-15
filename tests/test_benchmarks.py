"""Benchmark tests for FastAPI performance"""

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient
from typing import Optional


@pytest.fixture
def app():
    """Create FastAPI app for benchmarking"""
    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}
    
    @app.post("/items/")
    def create_item(item: dict):
        return {"item": item, "created": True}
    
    return app


@pytest.fixture
def client(app):
    """Create test client"""
    return TestClient(app)


def test_root_endpoint_performance(benchmark, client):
    """Benchmark root endpoint performance"""
    result = benchmark(client.get, "/")
    assert result.status_code == 200


def test_parameterized_endpoint_performance(benchmark, client):
    """Benchmark parameterized endpoint performance"""
    result = benchmark(client.get, "/items/42", params={"q": "test"})
    assert result.status_code == 200


def test_json_post_performance(benchmark, client):
    """Benchmark JSON POST performance"""
    payload = {"name": "Test", "price": 29.99}
    result = benchmark(client.post, "/items/", json=payload)
    assert result.status_code == 200


def test_app_startup_performance(benchmark):
    """Benchmark FastAPI app startup time"""
    def create_app():
        app = FastAPI()
        
        @app.get("/")
        def read_root():
            return {"Hello": "World"}
        
        return app
    
    app = benchmark(create_app)
    assert app is not None
