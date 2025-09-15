"""Memory profiling test for FastAPI components"""

from memory_profiler import profile
from fastapi import FastAPI
from starlette.testclient import TestClient
from typing import Optional
import json


@profile
def test_memory_usage():
    """Profile memory usage of FastAPI operations"""
    
    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}
    
    client = TestClient(app)
    
    for i in range(1000):
        response = client.get("/")
        assert response.status_code == 200
        
        response = client.get(f"/items/{i}?q=test{i}")
        assert response.status_code == 200
    
    print("Memory profiling completed")


if __name__ == "__main__":
    test_memory_usage()
