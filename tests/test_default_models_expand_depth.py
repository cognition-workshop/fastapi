from fastapi import FastAPI
from fastapi.testclient import TestClient


def test_default_models_expand_depth_included():
    app = FastAPI()

    @app.get("/test")
    def test_endpoint():
        return {"test": "value"}

    client = TestClient(app)
    response = client.get("/docs")
    assert response.status_code == 200
    assert '"defaultModelsExpandDepth": -1,' in response.text, (
        "default defaultModelsExpandDepth should be included"
    )


def test_custom_models_expand_depth_override():
    app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": 0})

    @app.get("/test")
    def test_endpoint():
        return {"test": "value"}

    client = TestClient(app)
    response = client.get("/docs")
    assert response.status_code == 200
    assert '"defaultModelsExpandDepth": 0,' in response.text, (
        "custom defaultModelsExpandDepth should override default"
    )
    assert '"defaultModelsExpandDepth": -1' not in response.text, (
        "default value should not appear when overridden"
    )
