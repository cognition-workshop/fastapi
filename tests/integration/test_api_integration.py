from typing import Optional

import pytest
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.testclient import TestClient


class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


def create_integration_test_app():
    app = FastAPI(title="Integration Test API", version="1.0.0")

    items_db = []

    @app.get("/")
    def read_root():
        return {"message": "Integration Test API", "version": "1.0.0"}

    @app.get("/health")
    def health_check():
        return {"status": "healthy", "items_count": len(items_db)}

    @app.post("/items/", response_model=dict)
    def create_item(item: Item):
        item_dict = item.model_dump()
        item_dict["id"] = len(items_db) + 1
        items_db.append(item_dict)
        return {"item": item_dict, "message": "Item created successfully"}

    @app.get("/items/")
    def read_items(skip: int = 0, limit: int = 10):
        return {"items": items_db[skip : skip + limit], "total": len(items_db)}

    @app.get("/items/{item_id}")
    def read_item(item_id: int):
        for item in items_db:
            if item["id"] == item_id:
                return {"item": item}
        return {"error": "Item not found"}, 404

    return app


@pytest.fixture
def client():
    app = create_integration_test_app()
    return TestClient(app)


class TestAPIIntegration:
    def test_api_health_and_root(self, client):
        root_response = client.get("/")
        assert root_response.status_code == 200
        assert "message" in root_response.json()

        health_response = client.get("/health")
        assert health_response.status_code == 200
        assert health_response.json()["status"] == "healthy"

    def test_item_crud_workflow(self, client):
        item_data = {
            "name": "Test Item",
            "price": 29.99,
            "description": "A test item for integration testing",
        }

        create_response = client.post("/items/", json=item_data)
        assert create_response.status_code == 200
        created_item = create_response.json()
        assert "item" in created_item
        assert created_item["item"]["name"] == item_data["name"]
        item_id = created_item["item"]["id"]

        get_response = client.get(f"/items/{item_id}")
        assert get_response.status_code == 200
        retrieved_item = get_response.json()
        assert retrieved_item["item"]["name"] == item_data["name"]

        list_response = client.get("/items/")
        assert list_response.status_code == 200
        items_list = list_response.json()
        assert items_list["total"] >= 1
        assert len(items_list["items"]) >= 1

    def test_api_error_handling(self, client):
        nonexistent_item_response = client.get("/items/999")
        assert nonexistent_item_response.status_code == 200

        invalid_item_response = client.post("/items/", json={"invalid": "data"})
        assert invalid_item_response.status_code == 422

    def test_api_pagination(self, client):
        for i in range(5):
            item_data = {"name": f"Item {i}", "price": 10.0 + i}
            client.post("/items/", json=item_data)

        paginated_response = client.get("/items/?skip=2&limit=2")
        assert paginated_response.status_code == 200
        items = paginated_response.json()["items"]
        assert len(items) <= 2

    def test_openapi_documentation(self, client):
        openapi_response = client.get("/openapi.json")
        assert openapi_response.status_code == 200
        openapi_spec = openapi_response.json()
        assert "openapi" in openapi_spec
        assert "info" in openapi_spec
        assert openapi_spec["info"]["title"] == "Integration Test API"
